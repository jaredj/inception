import sys
from .file_parser import parse_content_block
from .file_writer import write_files

def decode_content_block():
    print("Paste the CONTENT BLOCK here and add a line with '# NO MORE FILES FROM CHATGPT' at the end:")
    content_block = ""
    for line in sys.stdin:
        content_block += line
        if line.strip() == "# NO MORE FILES FROM CHATGPT":
            break

    file_contents = parse_content_block(content_block)
    write_files(file_contents)

if __name__ == "__main__":
    decode_content_block()
