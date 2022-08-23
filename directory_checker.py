import glob
dir = '/Users/akifislam/Downloads'
def has_already_downloaded():

    file_count = 0

    for cur_path in glob.glob(dir+"/**", recursive = True):
        if cur_path.endswith(".mp3"):
            file_count += 1
        if cur_path.endswith(".mp3.part"):
            file_count-=1
            print(" .mp3.part file exist")

    print("No. of. Files : ", file_count)
    return file_count


def is_song_exist(song_name):
    has_partial_file = False
    is_fully_downloaded = False

    for cur_path in glob.glob(dir+"/**", recursive = True):
        if cur_path.__contains__(song_name) and cur_path.endswith(".mp3"):
            is_fully_downloaded = True
        if cur_path.__contains__(song_name) and cur_path.endswith(".mp3.part"):
            has_partial_file = True

    if(has_partial_file == False and is_fully_downloaded == True):
        return True
    else:
        return False
