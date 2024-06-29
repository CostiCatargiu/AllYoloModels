
from moviepy.editor import VideoFileClip


def convert_video_to_gif(input_path, output_path, start_time, end_time, max_width=500, fps=10):
    # Load the video file
    clip = VideoFileClip(input_path).subclip(start_time, end_time)

    # Resize the clip if it's wider than max_width
    if clip.size[0] > max_width:
        clip = clip.resize(width=max_width)

    # Set the frames per second (fps) for the GIF
    clip = clip.set_fps(fps)

    # Write the GIF file
    clip.write_gif(output_path)


# Specify the input video path, output GIF path, start and end times in seconds
input_video = '/home/constantin/Doctorat/YoloModels/YoloLib2/ExperimentalResults/YoloV5/infer/exp/VideoNightMixt.mp4'
output_gif = 'output_filename.gif'
start = 0  # Start time in seconds
end = 30  # End time in seconds

convert_video_to_gif(input_video, output_gif, start, end)

import subprocess

def optimize_gif(path):
    cmd = [
        'convert', path,  # Input GIF
        '-fuzz', '5%',    # Allows for slight color differences
        '-layers', 'Optimize',  # Optimize layers
        path  # Output GIF (overwrite)
    ]
    subprocess.run(cmd)

# After creating the GIF
optimize_gif(output_gif)
