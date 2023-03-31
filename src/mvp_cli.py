#!/usr/bin/env python3
from file_parser import parse_content_block, parse_command_block
from file_writer import write_files
from command_executor import execute_commands
import os

def main():
    content_block = input("Paste the CONTENT BLOCK here:\n")
    file_contents = parse_content_block(content_block)
    write_files(file_contents)

    command_block = input("Paste the COMMAND BLOCK here (or press Enter to skip):\n")
    if command_block:
        commands = parse_command_block(command_block)
        output = execute_commands(commands)
        print("\n# RESULTS")
        for result in output:
            print(result)

    with open("prompts/Reminder.md", "r") as f:
        reminder_block = f.read()
    print("\n# REMINDER")
    print(reminder_block)

    print("\n# DONE")

if __name__ == "__main__":
    main()

