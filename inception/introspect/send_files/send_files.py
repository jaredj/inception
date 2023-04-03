import argparse
import os
import sys
from .directory_tree import print_directory_tree
from .send_directory import send_directory

def send_files(file_list=None):
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    print("```")  # Add triple backticks
    if file_list:
        print("# CONTENT:")
        for file_path in file_list:
            send_directory(file_path)
    else:
        print("# CONTENT:")
        send_directory(".")
    print("# NO MORE FILES FROM CHATGPT")
    print("```")  # Add triple backticks
#    print("\nDirectory Tree:")
#    print_directory_tree(".", prefix='src')

def main():
    parser = argparse.ArgumentParser(description='Inception: the file-sending tool')
    parser.add_argument('file_list', nargs='*', default=None,
                        help='List of files and directories to send')
    args = parser.parse_args()

    send_files(args.file_list)

if __name__ == "__main__":
    main()

