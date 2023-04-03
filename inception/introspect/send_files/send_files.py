import os
import sys
from .directory_tree import print_directory_tree
from .send_directory import send_directory

def send_files():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    print("# CONTENT:")
    send_directory(".", prefix='src')
    print("# NO MORE FILES FROM CHATGPT")
    print("\nDirectory Tree:")
    print_directory_tree(".", prefix='src')

if __name__ == "__main__":
    send_files()

