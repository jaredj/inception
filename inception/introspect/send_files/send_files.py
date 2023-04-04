import argparse
import os
import sys
import pyperclip
from .send_file_or_directory import send_file_or_directory

def generate_content_block(file_list=None):
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    content_block = "```\n"  # Add triple backticks
    if file_list:
        content_block += "# CONTENT:\n"
        for file_path in file_list:
            content_block += send_file_or_directory(file_path)
    else:
        content_block += "# CONTENT:\n"
        content_block += send_file_or_directory(".")
    content_block += "# NO MORE FILES FROM CHATGPT\n"
    content_block += "```\n"  # Add triple backticks
    return content_block

def main():
    parser = argparse.ArgumentParser(description='Inception: the file-sending tool')
    parser.add_argument('file_list', nargs='*', default=None,
                        help='List of files and directories to send')
    args = parser.parse_args()

    content_block = generate_content_block(args.file_list)
    print(content_block)
    pyperclip.copy(content_block)

    # Count the number of lines in the content block
    num_lines = content_block.count('\n')

    print(f"{num_lines}-line CONTENT BLOCK copied to clipboard ✓")

if __name__ == "__main__":
    main()
