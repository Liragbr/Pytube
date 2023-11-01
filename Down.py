# download the pytube library
#  -- pip install pytube -- 
from pytube import YouTube

link = input("Enter video link: ")
yt = YouTube(link)


print("Title:", yt.title)
print("Description:", yt.description)
print("Length:", yt.length, "Seconds")
print("Rating:", yt.rating)

video_stream = yt.streams.get_highest_resolution()
video_stream.download()

print("Download completed:", yt.title)
