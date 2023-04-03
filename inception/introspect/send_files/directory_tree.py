import os


def print_directory_tree(path, prefix=''):
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.startswith('.'):
                print(f"{sub_indent}{f}")

