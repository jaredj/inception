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

if __name__ == "__main__":
    main()