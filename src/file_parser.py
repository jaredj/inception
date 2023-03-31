def parse_content_block(content_block):
    file_contents = {}
    lines = content_block.strip().split("\n")
    current_file = None

    for line in lines:
        if line.startswith("## WRITE THIS FILE"):
            current_file = line.split("## WRITE THIS FILE")[1].strip()
            file_contents[current_file] = []
        else:
            file_contents[current_file].append(line)

    return file_contents

def parse_command_block(command_block):
    commands = command_block.strip().split("\n")
    return commands

