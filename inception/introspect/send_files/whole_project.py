import itertools
import os
from .send_files import generate_content_block
from .file_contents import get_file_contents

BYTE_LIMIT = 1550
PREAMBLE = "I'm sending you some of my project contents:\n\n"
POSTAMBLE = "\n\n ... Don't do anything yet, stay tuned for more:"
PER_CHUNK_BYTE_LIMIT = BYTE_LIMIT - len(PREAMBLE) - len(POSTAMBLE)

def calculate_size(root, exclude=None):
    total_size = 0
    for path, dirs, files in os.walk(root):
        if exclude and path.startswith(exclude):
            continue
        for file in files:
            file_path = os.path.join(path, file)
            total_size += len(generate_content_block([file_path]))
    return total_size

def count_top_level_files_and_prompts(path):
    top_level_files_size = 0
    prompts_size = 0
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isfile(entry_path):
            top_level_files_size += len(generate_content_block([entry_path]))
        elif entry == "prompts":
            prompts_size = calculate_size(entry_path)
    return top_level_files_size, prompts_size

def find_optimal_groupings(subfolders, top_level_files_size, prompts_size):
    optimal_groupings = []
    min_messages = float('inf')
    for i in range(1, len(subfolders) + 1):
        for combination in itertools.combinations(subfolders, i):
            total_size = sum(combination) + top_level_files_size + prompts_size
            messages = -(-total_size // PER_CHUNK_BYTE_LIMIT)  # Ceiling division
            if messages < min_messages:
                optimal_groupings = [combination]
                min_messages = messages
            elif messages == min_messages:
                optimal_groupings.append(combination)
    return optimal_groupings

def send_groupings(groupings, project_path):
    for grouping in groupings:
        message = PREAMBLE
        for size in grouping:
            for path, dirs, files in os.walk(project_path):
                for file in files:
                    file_path = os.path.join(path, file)
                    if len(generate_content_block([file_path])) == size:
                        message += generate_content_block([file_path])
        message += POSTAMBLE
        print(message)
        pyperclip.copy(message)
        input("Press Enter to continue...")

def send_whole_project():
    project_path = "."
    exclude = os.path.join(project_path, 'prompts')
    subfolders = [calculate_size(os.path.join(project_path, d), exclude) for d in os.listdir(project_path) if os.path.isdir(os.path.join(project_path, d)) and d != 'prompts']
    top_level_files_size, prompts_size = count_top_level_files_and_prompts(project_path)
    optimal_groupings = find_optimal_groupings(subfolders, top_level_files_size, prompts_size)
    selected_grouping = sorted(optimal_groupings, key=lambda x: sum(x))[0]
    send_groupings(selected_grouping, project_path)

    prompts_content_block_path = os.path.join(project_path, 'prompts', 'content-blocks.md')
    prompts_content_block = generate_content_block([prompts_content_block_path])
    print(prompts_content_block)
    pyperclip.copy(prompts_content_block)
    input("Press Enter to continue...")

if __name__ == "__main__":
    send_whole_project()

