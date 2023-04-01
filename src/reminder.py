## WRITE THIS FILE src/reminder.py
import os

def print_reminder():
    reminder_file = "prompts/Reminder.md"
    if os.path.exists(reminder_file):
        with open(reminder_file, 'r') as file:
            print("```\n")
            print(file.read().strip())
            print("\n```")
    else:
        print("Reminder file not found.")

