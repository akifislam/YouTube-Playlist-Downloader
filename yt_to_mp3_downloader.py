import glob
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from yt_playlist_scraper import get_song_links
from directory_checker import has_already_downloaded
from yt_playlist_scraper import get_song_names
from directory_checker import is_song_exist

PLAYLIST_LINK = "https://www.youtube.com/playlist?list=PLB-0AGqg4hO84subKqW5clqSDZmBpoLb7"
download_directory = "/Users/akifislam/Downloads"
songs = get_song_links(PLAYLIST_LINK)
songs_titles = get_song_names(PLAYLIST_LINK)
time.sleep(10)



for i in range(0,len(songs),1):

    print("#: ",i)
    song_link = songs[i] # To avoid double .png
    song_title = songs_titles[i]
    print("Song Name : ", songs_titles[i])
    print("Song URL : ",songs[i])
    if(is_song_exist(song_title)):
        print("This song has been already downloaded :)")
        print()
        continue
    try:
        driver = webdriver.Firefox(executable_path='/Users/akifislam/SeleniumEngines/geckodriver')

        driver.get("https://en.y2mate.is/35/youtube-to-mp3.html") # loadings page
        cur_mp3_count = has_already_downloaded()
        print("Initial File Count : ",cur_mp3_count)
        time.sleep(2)
        driver.maximize_window()
        driver.find_element(By.ID,'txtUrl').send_keys(song_link) #loading song URL
        time.sleep(1)
        driver.find_element(By.ID,'btnSubmit').click() #click submit button
        time.sleep(5)
        driver.find_element(By.ID,'btn251003003').click() #click convert button
        time.sleep(10)
        driver.find_element(By.ID,'btn251003003').click()

        timeout = 0
        while(not is_song_exist(song_title) and timeout<15):
            time.sleep(10)
            timeout += 1
            print("Downloading...")

        print(str(song_title) + " has been fully downloaded")

        driver.close()

    except:
        print("No Internet Connection, Trying Again Index ",i)
        i-=1