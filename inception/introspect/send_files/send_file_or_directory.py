import os
from .file_contents import get_file_contents
from .send_directory import send_directory

def send_file_or_directory(path, fallback_encoding='utf-8'):
    if os.path.isfile(path):
        print(f"## WRITE THIS FILE {path}")
        content = get_file_contents(path, fallback_encoding)
        if content is None:
            return
        print(content)
    elif os.path.isdir(path):
        send_directory(path, prefix=path, fallback_encoding=fallback_encoding)
