from moviepy.editor import VideoFileClip, concatenate_videoclips

def extract_and_combine_parts(input_path, output_path, time_segments):
    # Load the video file
    video = VideoFileClip(input_path)

    # Create a list to hold all the video clips
    clips = []

    # Extract each specified part and add it to the clips list
    for start_time, end_time in time_segments:
        clip = video.subclip(start_time, end_time)
        clips.append(clip)

    # Concatenate all the video clips into one video
    final_clip = concatenate_videoclips(clips, method="compose")

    # Write the result to the output file
    final_clip.write_videofile(output_path, codec='libx264')  # You can change the codec if needed

# Example usage:
input_video_path = '/home/constantin/Videos/Screencasts/Screencast from 23.06.2024 17:23:24.webm'
output_video_path = '/home/constantin/Videos/Screencasts/Screencastttt.mp4'
# time_segments = [(0, 35),(120, 130), (240, 270)]  # List of tuples (start_time, end_time) in seconds
# time_segments = [(30, 33), (65, 68), (119, 122), (190,193), (250,253), (320, 323), (392,396), (447,450),(560,563), (590,593)]  # List of tuples (start_time, end_time) in seconds
time_segments = [(4, 197)]  # List of tuples (start_time, end_time) in seconds

extract_and_combine_parts(input_video_path, output_video_path, time_segments)