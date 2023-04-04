import sys
from .file_parser import parse_content_block
from .file_writer import write_files
from ..git.integrate_git import integrate_git_operations

def decode_content_block(content_block, git_operations=False):
    commit_message, file_contents = parse_content_block(content_block)
    write_files(file_contents)

    files_changed = 0
    if git_operations:
        for file_path in file_contents.keys():
            if not commit_message:
                commit_message = f"Update {file_path} with ChatGPT generated code"
            file_changed = integrate_git_operations(file_path, commit_message)
            if file_changed:
                files_changed += 1

    if git_operations and files_changed == 0:
        print("No files have been updated in this content block.")

def prompt_and_decode_content_block():
    while True:
        print("Paste the CONTENT BLOCK here and add a line with '# NO MORE FILES FROM CHATGPT' at the end:")
        content_block = ""
        try:
            for line in sys.stdin:
                content_block += line
                if line.strip() == "# NO MORE FILES FROM CHATGPT":
                    break
        except KeyboardInterrupt:
            break
        except EOFError:
            break

        decode_content_block(content_block)

if __name__ == "__main__":
    prompt_and_decode_content_block()
