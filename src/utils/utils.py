import re
import os

def get_numbers_from_string(string: str):
    temp = re.findall(r'\d+', string) 
    return list(map(int, temp)) 

def get_all_files_from_path(path: str):
    result = []
    everything = os.listdir(path)
    for obj in everything:
        if os.path.isfile(obj):
            result.append(obj)
    return sorted(result)