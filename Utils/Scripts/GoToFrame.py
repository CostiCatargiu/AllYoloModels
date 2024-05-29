import cv2


def go_to_frame(video_path, frame_number):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_number >= total_frames:
        print(f"Error: Frame number {frame_number} is out of range. Total frames: {total_frames}.")
        return

    # Set the frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the frameq
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        return

    # Display the frame
    cv2.imshow(f'Frame {frame_number}', frame)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# Example usage
video_path = '/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloV5/infer/exp50/mergedd_video.mp4'
frame_number = 207# Change this to the frame number you want to go to
go_to_frame(video_path, frame_number)
