import re
import os


def get_numbers_from_string(string: str):
    temp = re.findall(r"\d+", string) 
    return list(map(int, temp)) 


def get_all_files_and_folder_from_path(path: str):
    return sorted(os.listdir(path))

# Refactor: array of extensions
def get_all_files_and_folder_from_path_keep_extension(path: str, extension: str):
    result = []
    values = get_all_files_and_folder_from_path(path)
    for value in values:
        if extension in value:
            result.append(value)
    return result

# path = os.getcwd()
def create_necessities():
    create_directories()

def create_directories():
    if not os.path.exists(".tmp"):
        os.mkdir(".tmp")
    if not os.path.exists(".tmp/videos"):
        os.mkdir(".tmp/videos")
    if not os.path.exists(".tmp/images"):
        os.mkdir(".tmp/images")
    if not os.path.exists(".tmp/audio"):
        os.mkdir(".tmp/audio")
    if not os.path.exists("output"):
        os.mkdir("output")


def clear_directories(path :str):
    if os.path.exists(path):
        rm_rec(path)
        os.rmdir(path)


def rm_rec(path: str):
    for f in os.scandir(path):
        if f.is_dir():
            rm_rec(f.path)
            os.rmdir(f.path)
        else:
            os.remove(f.path)

def concat_args(*argv):
    result = ""
    for arg in argv: 
        result += str(arg) + " "
    return result
