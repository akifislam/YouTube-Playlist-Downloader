from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

# Parsing YouTube Playlist URL
def get_songs(URL):
    song_links = Playlist(URL)
    return song_links


