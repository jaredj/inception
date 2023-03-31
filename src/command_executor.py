import os

def execute_commands(commands):
    output = []
    for command in commands:
        if command.startswith("cat"):
            file_path = command.split("cat")[1].strip()
            with open(file_path, 'r') as f:
                output.append(f.read())
        elif command.startswith("ls"):
            directory = command.split("ls")[1].strip() or "."
            output.append("\n".join(os.listdir(directory)))

    return output
