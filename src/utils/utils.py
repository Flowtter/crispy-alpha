import re

def get_numbers_from_string(string: str):
    temp = re.findall(r'\d+', string) 
    return list(map(int, temp)) 