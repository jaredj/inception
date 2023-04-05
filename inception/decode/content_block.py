import sys
from .file_parser import parse_content_block
from .file_writer import write_files
from ..git.integrate_git import (
    integrate_git_operations, 
    create_and_checkout_inception_branch,
    print_diff_stats,
    print_merge_instructions,
    get_current_branch_name,
)

def decode_content_block(content_block, git_operations=False):
    commit_message, file_contents = parse_content_block(content_block)
    write_files(file_contents)

    if git_operations:
        current_branch = get_current_branch_name()
        if current_branch in ["main", "master"]:
            branch_name = create_and_checkout_inception_branch(commit_message)
        elif "incept-" in current_branch:
            branch_name = current_branch
        else:
            print(f"WARNING: Not in 'main', 'master', or 'incept-*' branch. Changes will not be committed.")
            return

        for file_path in file_contents.keys():
            if not commit_message:
                commit_message = f"Update {file_path} with ChatGPT generated code"
            files_changed = integrate_git_operations(file_path, commit_message)
            print_diff_stats(files_changed, branch_name)

        print_merge_instructions(branch_name)

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

        decode_content_block(content_block, git_operations=True)

if __name__ == "__main__":
    prompt_and_decode_content_block()
