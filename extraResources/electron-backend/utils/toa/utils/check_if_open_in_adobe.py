import os


def check_if_open_in_adobe(combined_path):
    try:
        os.rename(combined_path, combined_path)
        return False
    except:
        return True
