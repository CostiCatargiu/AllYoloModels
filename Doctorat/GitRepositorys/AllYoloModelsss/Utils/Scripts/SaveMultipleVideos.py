import subprocess

def create_video_grid(clip1, clip2, clip3, clip4, output, speed=1.0):
    # Full HD resolution
    width, height = 1920, 1080

    # Define the ffmpeg command
    ffmpeg_command = [
        'ffmpeg',
        '-i', clip1, '-i', clip2, '-i', clip3, '-i', clip4,
        '-filter_complex',
        f"""
        [0:v] setpts={1/speed}*PTS, scale={width//2}:{height//2} [a];
        [1:v] setpts={1/speed}*PTS, scale={width//2}:{height//2} [b];
        [2:v] setpts={1/speed}*PTS, scale={width//2}:{height//2} [c];
        [3:v] setpts={1/speed}*PTS, scale={width//2}:{height//2} [d];
        [a][b] hstack=inputs=2 [top];
        [c][d] hstack=inputs=2 [bottom];
        [top][bottom] vstack=inputs=2 [output]
        """,
        '-map', '[output]',
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-crf', '23',
        '-y',  # Overwrite output file if it exists
        output
    ]

    # Run the ffmpeg command
    subprocess.run(ffmpeg_command)

if __name__ == "__main__":
    # Paths to your video clips
    clip1 = 'path/to/clip1.mp4'
    clip2 = 'path/to/clip2.mp4'
    clip3 = 'path/to/clip3.mp4'
    clip4 = 'path/to/clip4.mp4'

    # Output video path
    output = 'output.mp4'

    # Speed factor (e.g., 2.0 for double speed, 0.5 for half speed)
    speed = 1.5  # Adjust the speed factor as needed

    # Create the video grid with speed adjustment
    create_video_grid(clip1, clip2, clip3, clip4, output, speed)

    print(f"Output video saved as {output}")

if __name__ == "__main__":
    # Paths to your video clips
    clip1 = '/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloV5/infer/exp_day/VideoDayMixt.mp4'
    clip2 = '/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloV6/infer/exp_bestday/VideoDayMixt.mp4'
    clip3 = '/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloV7/infer/exp_bestday/VideoDayMixt.mp4'
    clip4 = '/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloV8/infer/expbest_day/VideoDayMixt.avi'

    speed = 2  # Adjust the speed factor as needed

    # Output video path
    output = 'output.mp4'

    # Create the video grid
    create_video_grid(clip1, clip2, clip3, clip4, output, speed)

    print(f"Output video saved as {output}")
