#!/usr/bin/env python3
import sys
from cli_functions import handle_instruction, handle_comment, handle_skip
from file_parser import parse_content_block, parse_command_block
from file_writer import write_files
from command_executor import execute_commands
from reminder import print_reminder

def main():
    choice = input("Press 'i' for INSTRUCTION, 'c' for COMMENT, or 's' for SKIP: ").lower()

    if choice == 'i':
        handle_instruction()
    elif choice == 'c':
        handle_comment()
    elif choice == 's':
        handle_skip()
    else:
        print("Invalid choice.")
        return

    print_reminder()

    print("Paste the CONTENT BLOCK here and add a line with '# NO MORE FILES FROM CHATGPT' at the end:")
    content_block = ""
    for line in sys.stdin:
        content_block += line
        if line.strip() == "# NO MORE FILES FROM CHATGPT":
            break

    file_contents = parse_content_block(content_block)
    write_files(file_contents)

    command_block = input("Paste the COMMAND BLOCK here (or press Enter to skip):\n")
    if command_block:
        commands = parse_command_block(command_block)
        output = execute_commands(commands)
        print("\n# RESULTS")
        for result in output:
            print(result)

    print("\n# DONE")

if __name__ == "__main__":
    main()

