from pytube import YouTube
import os

def download_mp4(URL,directory_to_save):
    yt = YouTube(str(URL))
    video = yt.streams.filter(progressive=True).get_highest_resolution()
    destination = str(directory_to_save) or '.'
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")

