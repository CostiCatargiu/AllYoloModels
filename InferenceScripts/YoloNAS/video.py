from typing import List, Optional, Tuple, Iterable, Iterator
import cv2, sys
import PIL

import numpy as np


from super_gradients.common.abstractions.abstract_logger import get_logger

import supervision as sv
from supervision.geometry.core import Point
from supervision.draw.utils import draw_text
import os, cv2
from collections import deque
import numpy as np

sys.path.append('../../InferenceScripts')
from UtilFunctions import CalcFPS, set_parameters

logger = get_logger(__name__)

__all__ = ["load_video", "save_video", "includes_video_extension", "show_video_from_disk", "show_video_from_frames"]

VIDEO_EXTENSIONS = (".mp4", ".avi", ".mov", ".wmv", ".flv", ".gif")


def load_video(file_path: str, max_frames: Optional[int] = None) -> Tuple[List[np.ndarray], int]:
    """Open a video file and extract each frame into numpy array.

    :param file_path:   Path to the video file.
    :param max_frames:  Optional, maximum number of frames to extract.
    :return:
                - Frames representing the video, each in (H, W, C), RGB.
                - Frames per Second (FPS).
    """
    cap = _open_video(file_path)
    frames = _extract_frames(cap, max_frames)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return frames, fps


def lazy_load_video(file_path: str, max_frames: Optional[int] = None) -> Tuple[Iterator[np.ndarray], int, int]:
    """Open a video file and returns a generator which yields frames.

    :param file_path:   Path to the video file.
    :param max_frames:  Optional, maximum number of frames to extract.
    :return:
                - Generator yielding frames representing the video, each in (H, W, C), RGB.
                - Frames per Second (FPS).
                - Amount of frames in video.
    """
    cap = _open_video(file_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = _lazy_extract_frames(cap, max_frames)
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return frames, fps, num_frames


def _open_video(file_path: str) -> cv2.VideoCapture:
    """Open a video file.

    :param file_path:   Path to the video file
    :return:            Opened video capture object
    """
    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        raise ValueError(f"Failed to open video file: {file_path}")
    return cap


def _extract_frames(cap: cv2.VideoCapture, max_frames: Optional[int] = None) -> List[np.ndarray]:
    """Extract frames from an opened video capture object.

    :param cap:         Opened video capture object.
    :param max_frames:  Optional maximum number of frames to extract.
    :return:            Frames representing the video, each in (H, W, C), RGB.
    """
    frames = []

    while max_frames != len(frames):
        frame_read_success, frame = cap.read()
        if not frame_read_success:
            break
        frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    return frames


def _lazy_extract_frames(cap: cv2.VideoCapture, max_frames: Optional[int] = None) -> Iterator[np.ndarray]:
    """Lazy implementation of frames extraction from an opened video capture object.
    NOTE: Releases the capture object.

    :param cap:         Opened video capture object.
    :param max_frames:  Optional maximum number of frames to extract.
    :return:            Generator yielding frames representing the video, each in (H, W, C), RGB.
    """
    frames_counter = 0

    while frames_counter != max_frames:
        frame_read_success, frame = cap.read()
        if not frame_read_success:
            break

        frames_counter += 1
        yield cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cap.release()


def save_video(output_path: str, frames: List[np.ndarray], fps: int) -> None:
    """Save a video locally. Depending on the extension, the video will be saved as a .mp4 file or as a .gif file.

    :param output_path: Where the video will be saved
    :param frames:      Frames representing the video, each in (H, W, C), RGB. Note that all the frames are expected to have the same shape.
    :param fps:         Frames per second
    """
    if not includes_video_extension(output_path):
        logger.info(f'Output path "{output_path}" does not have a video extension, and therefore will be saved as {output_path}.mp4')
        output_path += ".mp4"

    if check_is_gif(output_path):
        save_gif(output_path, frames, fps)
    else:
        save_mp4(output_path, frames, fps)


def save_gif(output_path: str, frames: Iterable[np.ndarray], fps: int) -> None:
    """Save a video locally in .gif format. Safe for generator of frames object.

    :param output_path: Where the video will be saved
    :param frames:      Frames representing the video, each in (H, W, C), RGB. Note that all the frames are expected to have the same shape.
    :param fps:         Frames per second
    """
    frame_iter_obj = iter(frames)
    pil_frames_iter_obj = map(PIL.Image.fromarray, frame_iter_obj)

    first_frame = next(pil_frames_iter_obj)

    first_frame.save(output_path, save_all=True, append_images=pil_frames_iter_obj, duration=int(1000 / fps), loop=0)


def save_mp4(output_path: str, frames: Iterable[np.ndarray], fps: int) -> None:
    """Save a video locally in .mp4 format. Safe for generator of frames object.

    :param output_path: Where the video will be saved
    :param frames:      Frames representing the video, each in (H, W, C), RGB. Note that all the frames are expected to have the same shape.
    :param fps:         Frames per second
    """
    video_height, video_width, video_writer = None, None, None

    for frame in frames:
        if video_height is None:
            video_height, video_width = frame.shape[:2]
            video_writer = cv2.VideoWriter(
                output_path,
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps,
                (video_width, video_height),
            )
        _validate_frame(frame, video_height, video_width)
        video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    video_writer.release()


def _validate_frame(frame: np.ndarray, control_height: int, control_width: int) -> None:
    """Validate the frame to make sure it has the correct size and includes the channel dimension. (i.e. (H, W, C))

    :param frame:  Single frame from the video, in (H, W, C), RGB.
    """
    height, width = frame.shape[:2]

    if (height, width) != (control_height, control_width):
        raise RuntimeError(
            f"Current frame has resolution {height}x{width} but {control_height}x{control_width} is expected!"
            f"Please make sure that all the frames have the same shape."
        )

    if frame.ndim != 3:
        raise RuntimeError("Your frames must include 3 channels.")


def show_video_from_disk(video_path: str, window_name: str = "Prediction"):
    """Display a video from disk using OpenCV.

    :param video_path:   Path to the video file.
    :param window_name:  Name of the window to display the video
    """
    cap = _open_video(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            # Display the frame
            cv2.imshow(window_name, frame)

            # Wait for the specified number of milliseconds before displaying the next frame
            if cv2.waitKey(int(1000 / fps)) & 0xFF == ord("q"):
                break
        else:
            break

    # Release the VideoCapture object and destroy the window
    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def show_video_from_frames(frames: List[np.ndarray], fps: float, window_name: str = "Prediction") -> None:
    """Display a video from a list of frames using OpenCV.

    :param frames:      Frames representing the video, each in (H, W, C), RGB. Note that all the frames are expected to have the same shape.
    :param fps:         Frames per secondqqqqqqqqqqqqqqq
    :param window_name:  Name of the window to display the video
    """
    text_anchor6, text_anchor7, text_overlay7, anchor_list1, anchor_list, classesCount, text_anchor, text_anchor1, text_anchor2, text_anchor3, text_anchor5, text_anchor4, text_overlay5, text_overlay6, text_overlay, text_overlay2, text_overlay4, text_color, text_scale, text_thickness, background_color = set_parameters()
    for frame in frames:
        with open("/home/constantin/Doctorat/YoloModels/YoloLib2/InferenceScripts/infos.txt", 'r') as f:
            line1 = f.readline().strip()  # Read and strip whitespace
            value1 = float(line1)
            line2 = f.readline().strip()  # Read and strip whitespace
            value2 = float(line2)
            line3 = f.readline().strip()

        elements = line3.split(',')
        element_counts = {}
        for element in elements:
            if element in element_counts:
                element_counts[element] += 1
            else:
                element_counts[element] = 1
        result_list = []
        for element, count in element_counts.items():
            result_list.extend([str(count), element])

        inference_time = value1
        avg_fps = value2
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.resize(frame, (1200, 800))  # Resize the frame

        inference_time_ms = inference_time * 1000
        text_overlay3 = f'{avg_fps:.2f}'
        text_overlay1 = f'{inference_time_ms:.2f}'

        annotated_frame = draw_text(scene=frame, text=text_overlay, text_anchor=text_anchor,
                                    text_color=text_color, background_color=background_color,
                                    text_thickness=text_thickness, text_scale=text_scale)
        annotated_frame = draw_text(scene=annotated_frame, text=text_overlay1, text_anchor=text_anchor1,
                                    text_color=text_color, background_color=background_color,
                                    text_thickness=text_thickness, text_scale=text_scale)
        annotated_frame = draw_text(scene=annotated_frame, text=text_overlay2, text_anchor=text_anchor2,
                                    text_color=text_color, background_color=background_color,
                                    text_thickness=text_thickness, text_scale=text_scale)
        annotated_frame = draw_text(scene=annotated_frame, text=text_overlay3, text_anchor=text_anchor3,
                                    text_color=text_color, background_color=background_color,
                                    text_thickness=text_thickness, text_scale=text_scale)
        annotated_frame = draw_text(scene=annotated_frame, text=text_overlay4, text_anchor=text_anchor4,
                                    text_color=sv.Color.RED, background_color=background_color,
                                    text_thickness=1, text_scale=0.5)
        annotated_frame = draw_text(scene=annotated_frame, text=text_overlay5, text_anchor=text_anchor5,
                                    text_color=sv.Color.RED, background_color=background_color,
                                    text_thickness=1, text_scale=0.4)

        countFlag = os.environ.get('COOUNT_FLAG')
        countFlag = 'ok'
        classesCount =['car','person','traffic light']
        if countFlag == 'ok':
            nr_dets = []
            for i in range(0, len(classesCount)):
                ok = 0
                for j in range(0, (len(result_list))):
                    if result_list[j] == classesCount[i] or str(result_list[j])[:-1] == classesCount[i]:
                        nr_dets.append(str(result_list[j - 1]))
                        ok = 1
                if ok == 0:
                    nr_dets.append('0')

            # print(nr_dets)
            # res = [eval(i) for i in nr_dets]

            # total_det=sum(nr_dets)
            total_det = sum([int(i) for i in nr_dets if type(i) == int or i.isdigit()])
            total_det = str(total_det)
            for i in range(0, len(classesCount)):
                annotated_frame = draw_text(scene=annotated_frame, text=classesCount[i] + ':',
                                            text_anchor=anchor_list[i],
                                            text_color=sv.Color.RED, background_color=background_color,
                                            text_thickness=2, text_scale=0.6)

            for i in range(0, len(classesCount)):
                annotated_frame = draw_text(scene=annotated_frame, text=nr_dets[i], text_anchor=anchor_list1[i],
                                            text_color=sv.Color.RED, background_color=background_color,
                                            text_thickness=2, text_scale=0.6)

            annotated_frame = draw_text(scene=annotated_frame, text=text_overlay7, text_anchor=text_anchor6,
                                        text_color=sv.Color.RED, background_color=background_color,
                                        text_thickness=2, text_scale=0.6)

            annotated_frame = draw_text(scene=annotated_frame, text=total_det, text_anchor=text_anchor7,
                                        text_color=sv.Color.RED, background_color=background_color,
                                        text_thickness=2, text_scale=0.6)

        # cv2.imshow("Image", annotated_frame)
        cv2.imshow(window_name, annotated_frame)
        if cv2.waitKey(int(1000 / fps)) & 0XFF == ord('q'):
            exit(1)


def includes_video_extension(file_path: str) -> bool:
    """Check if a file includes a video extension.
    :param file_path:   Path to the video file.
    :return:            True if the file includes a video extension.
    """
    return isinstance(file_path, str) and file_path.lower().endswith(VIDEO_EXTENSIONS)


def check_is_gif(file_path: str) -> bool:
    return file_path.lower().endswith(".gif")
