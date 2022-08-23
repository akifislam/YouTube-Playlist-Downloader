from yt_playlist_scraper import get_songs
from converter import download_mp4

print("Welcome to YouTube Video/Playlist Downloader.\nInsert 1 to download a single video (mp4)\nInsert 2 to download a playlist.\n")
user_input = int(input(""));

while(user_input!=1 and user_input!=2):
    user_input = int(input("Warning!\nInsert 1 to download a single video (mp4)\nInsert 2 to download a playlist.\n"))

if(user_input==2):
    YOUTUBE_PLAYLIST_URL = input("Enter the URL of your playlist :\n") or 'https://www.youtube.com/playlist?list=PLB-0AGqg4hO99EoYUGyaR4H-1zBqN5wvi'

    #Enter the directory address where you want to save songs
    download_directory = input("Enter the directory where you want to save (or simply put a '.' if you want to ignore):\n") or '.'
    print("Please wait ...")

    songs = get_songs(YOUTUBE_PLAYLIST_URL) #Enter the playlist link you want to download

    serial_count = 1

    for song in songs:
        print(str(serial_count)+".",end="")
        songURL = song # To avoid double .png
        download_mp4(songURL,download_directory)
        serial_count+=1
else:
    YOUTUBE_PLAYLIST_URL = input("Enter the URL of your video :\n") or 'https://www.youtube.com/playlist?list=PLB-0AGqg4hO99EoYUGyaR4H-1zBqN5wvi'
    download_directory = input("Enter the directory where you want to save (or simply put a '.' if you want to ignore):\n") or '.'
    download_mp4(YOUTUBE_PLAYLIST_URL,download_directory)
