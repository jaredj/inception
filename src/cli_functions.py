import sys

from getch import getch
from reminders import print_reminder


def handle_instruction():
    print("Provide an INSTRUCTION:")
    user_input = sys.stdin.readline().strip()
    print_block("INSTRUCTION", user_input)


def handle_comment():
    print("Provide a COMMENT:")
    user_input = sys.stdin.readline().strip()
    print_block("COMMENT", user_input)


def print_block(block_type, content):
    print(f"```{block_type}\n{content}\n```")


def main_menu():
    print("Press 'i' for INSTRUCTION, 'c' for COMMENT, or 's' for SKIP:")
    choice = getch()
    if choice == 'i':
        handle_instruction()
    elif choice == 'c':
        handle_comment()
    elif choice == 's':
        pass
    else:
        print("Invalid input. Please try again.")
