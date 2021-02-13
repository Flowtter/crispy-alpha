import re
import os


def get_numbers_from_string(string: str):
    temp = re.findall(r'\d+', string) 
    return list(map(int, temp)) 


# TODO : refactpr
def get_all_files_and_folder_from_path(path: str):
    return sorted(os.listdir(path))