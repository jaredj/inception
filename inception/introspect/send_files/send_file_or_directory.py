import os
from .send_directory import send_directory
from .file_contents import get_file_contents

def send_file_or_directory(file_path):
    if os.path.isdir(file_path):
        send_directory(file_path)
    elif os.path.isfile(file_path):
        print(f"## WRITE THIS FILE {file_path}")
        content = get_file_contents(file_path)
        if content is not None:
            print(content)

