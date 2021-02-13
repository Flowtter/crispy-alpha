import sys
from utils.utils import create_directories, clear_directories

create_directories()

# check first argument
if len(sys.argv) <= 1 or sys.argv[1] != '--keep':
    clear_directories()