import time

from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

# Parsing YouTube Playlist URL
def get_song_links(URL):
    song_links = Playlist(URL)
    return song_links

def get_song_names(URL):
    print("Please wait, All the URLS and Titles are pursing ...")
    try:
        play_list = Playlist(URL)
        song_titles = []

        for video in play_list.videos:
            song_titles.append(video.title)

        return song_titles
    except:
        print("Internet Failed in get_song_names function. Trying to re-connect ")
        time.sleep(10)
        get_song_names(URL)

# get_song_names("https://www.youtube.com/playlist?list=PLB-0AGqg4hO99EoYUGyaR4H-1zBqN5wvi")
