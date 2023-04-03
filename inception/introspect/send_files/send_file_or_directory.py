import os
from .file_contents import get_file_contents
from .send_directory import send_directory

def send_file_or_directory(path, fallback_encoding='utf-8'):
    content = ""
    if os.path.isfile(path):
        content += f"## WRITE THIS FILE {path}\n"
        file_content = get_file_contents(path, fallback_encoding)
        if file_content is None:
            return
        content += file_content + "\n"
    elif os.path.isdir(path):
        content += send_directory(path, prefix=path, fallback_encoding=fallback_encoding)
    return content
