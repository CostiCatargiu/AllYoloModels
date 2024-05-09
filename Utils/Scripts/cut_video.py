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
input_video_path = '/home/constantin/Doctorat/FireDataset/VideoTestFire/FireDay/foctudor.mp4'
output_video_path = '/home/constantin/Doctorat/FireDataset/VideoTestFire/FireDay/foctudor_cut.mp4'
# time_segments = [(0, 35),(120, 130), (240, 270)]  # List of tuples (start_time, end_time) in seconds
time_segments = [(10, 30), (60, 80)]  # List of tuples (start_time, end_time) in seconds

extract_and_combine_parts(input_video_path, output_video_path, time_segments)
