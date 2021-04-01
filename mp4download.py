# Downloading YouTube videos into mp4 files

# Install library
pip install pytube

# Import YouTube package
from pytube import YouTube

# Ask user for a video link
link = input("Cole o link aqui: ")

# Send video link into the package and assign the information into a variable
video = YouTube(link)

# Get the highest resolution of the video and store it
stream = video.streams.get_highest_resolution()

# Download the file
stream.download()
