import os
from concurrent.futures import ThreadPoolExecutor
from moviepy.editor import VideoFileClip

# Set input and output directories
input_dir = r'.....' # path to the directory containing .avi files
output_dir = r'.....' # path to the directory where .mp4 files will be saved

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def convert_video(input_file, output_file):
    """Function to convert a single video file."""
    with VideoFileClip(input_file) as video:
        video.write_videofile(output_file, codec='libx264', bitrate='800k')

# Collect all .avi files
avi_files = [f for f in os.listdir(input_dir) if f.endswith('.avi')]

# Use ThreadPoolExecutor to convert videos in parallel
with ThreadPoolExecutor() as executor:
    futures = []
    for filename in avi_files:
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.replace('.avi', '.mp4'))
        futures.append(executor.submit(convert_video, input_file, output_file))

    # Wait for all threads to complete
    for future in futures:
        future.result()
