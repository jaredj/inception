import os
import sys
from .directory_tree import print_directory_tree
from .send_directory import send_directory


def send_directory(path, prefix='', fallback_encoding='utf-8'):
    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in files:
            if not file.startswith("."):
                filepath = os.path.join(root, file)
                relpath = os.path.relpath(filepath, path)
                content = get_file_contents(filepath, fallback_encoding)
                if content is None:
                    print(f"## WRITE THIS FILE {os.path.join(prefix, relpath)}")
                    continue
                print(f"```{os.path.join(prefix, relpath)}```")
                print(content)


def send_files():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    print("# CONTENT:")
    send_directory(".", prefix='src')
    print("# NO MORE FILES FROM CHATGPT")
    print("\nDirectory Tree:")
    print_directory_tree(".", prefix='src')


if __name__ == "__main__":
    send_files()

