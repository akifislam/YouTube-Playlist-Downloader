import glob
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from yt_playlist_scraper import get_songs
from directory_checker import has_already_downloaded

songs = get_songs('https://www.youtube.com/playlist?list=PLB-0AGqg4hO99EoYUGyaR4H-1zBqN5wvi')
download_directory = "/Users/akifislam/Downloads/"
for song in songs:
    song_name = song # To avoid double .png
    print("Song URL : ", song_name)

    driver = webdriver.Firefox(executable_path='/Users/akifislam/SeleniumEngines/geckodriver')

    driver.get("https://en.y2mate.is/35/youtube-to-mp3.html") # loadings page
    cur_mp3_count = has_already_downloaded(download_directory)
    time.sleep(2)
    driver.maximize_window()
    driver.find_element(By.ID,'txtUrl').send_keys(song_name) #loading song URL
    time.sleep(5)
    driver.find_element(By.ID,'btnSubmit').click() #click submit button
    time.sleep(10)
    driver.find_element(By.ID,'btn251003003').click() #click convert button
    time.sleep(10)
    driver.find_element(By.ID,'btn251003003').click() #click download button

    while(cur_mp3_count == has_already_downloaded(download_directory)):
        time.sleep(10)

    driver.close()