def print_reminder():
    print("```\n# REMINDER")
    with open("Reminders.md", "r") as reminder_file:
        for line in reminder_file:
            print(line.strip())
    print("```")
