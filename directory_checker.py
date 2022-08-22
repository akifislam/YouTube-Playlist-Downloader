import glob

def has_already_downloaded(download_directory):

    file_count = 0

    for cur_path in glob.glob(download_directory+"/**", recursive = True):
        if cur_path.endswith(".mp3"):
            file_count += 1

    return file_count
