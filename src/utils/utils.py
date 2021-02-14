import re
import os


def get_numbers_from_string(string: str):
    temp = re.findall(r"\d+", string) 
    return list(map(int, temp)) 


def get_all_files_and_folder_from_path(path: str):
    return sorted(os.listdir(path))
import os


# path = os.getcwd()
def create_necessities():
    create_directories()

def create_directories():
    if not os.path.exists(".tmp"):
        os.mkdir(".tmp")
    if not os.path.exists(".tmp/videos"):
        os.mkdir(".tmp/videos")
    if not os.path.exists(".tmp/videos/output"):
        os.mkdir(".tmp/videos/output")
    if not os.path.exists(".tmp/images"):
        os.mkdir(".tmp/images")
    if not os.path.exists(".tmp/audio"):
        os.mkdir(".tmp/audio")


def clear_directories():
    if os.path.exists(".tmp"):
        rm_rec(".tmp")
        os.rmdir(".tmp")


def rm_rec(path: str):
    for f in os.scandir(path):
        if f.is_dir():
            rm_rec(f.path)
            os.rmdir(f.path)
        else:
            os.remove(f.path)
