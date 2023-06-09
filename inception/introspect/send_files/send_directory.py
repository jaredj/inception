import os
import sys
from .directory_tree import print_directory_tree
from .file_contents import get_file_contents


def send_directory(path, prefix='', fallback_encoding='utf-8'):
    content = ''
    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in files:
            if not file.startswith("."):
                filepath = os.path.join(root, file)
                relpath = os.path.relpath(filepath, path)
                content += f"## WRITE THIS FILE {os.path.join(prefix, relpath)}\n"
                file_content = get_file_contents(filepath, fallback_encoding)
                if file_content is None:
                    continue
                content += file_content + "\n"
    return content

