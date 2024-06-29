import os, cv2, re
def extract_frames(video_path, frame_indices, output_folder):
    # Check if the video file exists
    if not os.path.isfile(video_path):
        print(f"Error: The video file {video_path} does not exist.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}.")
        return

    frame_count = 0
    saved_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count in frame_indices:
            # Save the frame as a JPEG file
            frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
        frame_count += 1
        # Break early if we've saved all the requested frames
        if saved_count == len(frame_indices):
            break

    cap.release()


import os
import argparse

def find_video_and_create_folder(base_dir):
    video_path = None
    # Search for .avi or .mp4 files in the base directory
    for dirpath, _, filenames in os.walk(base_dir):
        for file in filenames:
            if file.endswith(('.mp4', '.avi')):
                video_path = os.path.join(dirpath, file)
                print(video_path)
                break
        if video_path:
            break

    if video_path is None:
        print("No video file found.")
        return None

    return video_path


import os
import time


def get_last_folder_by_creation_date(directory):
    # List all files and directories in the given directory
    items = os.listdir(directory)

    # Filter out files, keeping only directories
    folders = [item for item in items if os.path.isdir(os.path.join(directory, item))]

    # Sort the folders by creation date
    folders.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)), reverse=True)

    # Get the last folder
    if folders:
        last_folder = folders[0]
        last_folder_path = os.path.join(directory, last_folder)
        return last_folder_path
    else:
        return None


import os
import re
import cv2


def extract_confusion_frames(video_path, txt_file_path, output_directory):
    text_files = []
    for root, dirs, files in os.walk(txt_file_path):
        for file in files:
            if file.endswith(".txt"):
                text_files.append(file)


    file_path = os.path.join(txt_file_path, text_files[0])

    # Parse the txt file
    confusion_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                # Use regular expressions to extract the classes and frame numbers
                match = re.match(r"Frames in which (.+?) were predicted to be (.+?) or vice versa: \[(.+)\]", line)
                if match:
                    class1, class2, frames_str = match.groups()
                    frames = list(map(int, frames_str.split(',')))
                    confusion_data[(class1, class2)] = frames

    # Create output directories
    for classes in confusion_data:
        folder_name = f"{classes[0]}_{classes[1]}"
        folder_path = os.path.join(output_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Open video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    for classes, frames in confusion_data.items():
        folder_name = f"{classes[0]}_{classes[1]}"
        folder_path = os.path.join(output_directory, folder_name)

        for frame_num in frames:
            if frame_num >= frame_count:
                print(
                    f"Warning: Frame number {frame_num} exceeds the total frame count {frame_count}. Skipping this frame.")
                continue

            # Set the frame position
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            ret, frame = cap.read()

            if ret:
                frame_filename = os.path.join(folder_path, f"frame_{frame_num}.jpg")
                cv2.imwrite(frame_filename, frame)
            else:
                print(f"Error: Could not read frame {frame_num}.")

    cap.release()
    print("Frames extracted and saved successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find video file and create a folder.')
    parser.add_argument('base_dir', type=str, help='The base directory to search for video files.')

    args = parser.parse_args()

    last_folder_path = get_last_folder_by_creation_date(args.base_dir)
    print()
    video_path = find_video_and_create_folder(last_folder_path)
    extract_confusion_frames(video_path, last_folder_path, last_folder_path)

