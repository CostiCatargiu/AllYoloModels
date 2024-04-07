import supervision as sv
from supervision.geometry.core import Point
from supervision.draw.utils import draw_text
import os, cv2
from collections import deque
import numpy as np

def set_parameters():
    yolo_model = os.environ.get('PARAMETER')
    device_name = os.environ.get('DEVICE_PARAMETER')
    if 'NVIDIA' in device_name:
        text_anchor5 = Point(x=90, y=20)
    else:
        text_anchor5 = Point(x=135, y=20)
    text_anchor4 = Point(x=65, y=50)
    text_anchor = Point(x=40, y=80)
    text_anchor1 = Point(x=115, y=80)
    text_anchor2 = Point(x=40, y=110)
    text_anchor3 = Point(x=110, y=110)

    text_overlay = f'InfTime:'
    text_overlay2 = f'FPS:'
    text_overlay4 = f'Model: {yolo_model}'
    text_overlay5 = f'{device_name}'
    text_scale = 0.6
    text_thickness = 2
    text_color = sv.Color.ROBOFLOW
    background_color = sv.Color.WHITE

    return text_anchor, text_anchor1, text_anchor2, text_anchor3,text_anchor5, text_anchor4, text_overlay5, text_overlay, text_overlay2,text_overlay4,text_color,text_scale,text_thickness,background_color

def show_inference(inference_time, avg_fps, im0, p, text_anchor, text_anchor1, text_anchor2, text_anchor3,text_anchor5, text_anchor4, text_overlay5, text_overlay, text_overlay2,text_overlay4,text_color,text_scale,text_thickness,background_color):
    inference_time_ms = inference_time * 1000
    text_overlay3 = f'{avg_fps:.2f}'
    text_overlay1 = f'{inference_time_ms:.2f}'
    annotated_frame = draw_text(scene=im0, text=text_overlay, text_anchor=text_anchor,
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
    # cv2.imshow("Image", annotated_frame)
    cv2.imshow(str(p), annotated_frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        exit(1)

class CalcFPS:
    def __init__(self, nsamples: int = 25):
        self.framerate = deque(maxlen=nsamples)

    def update(self, duration: float):
        self.framerate.append(duration)

    def accumulate(self):
        if len(self.framerate) > 1:
            return np.average(self.framerate)
        else:
            return 0.0