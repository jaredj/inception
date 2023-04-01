#!/usr/bin/env python3
import os
import chardet
from pathlib import Path
import importlib
import pkgutil
from collections import deque

def send_directory(path, prefix='', fallback_encoding='utf-8'):
    for root, dirs, files in os.walk(path, topdown=True):
        # exclude hidden directories and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in files:
            # exclude hidden files
            if not file.startswith("."):
                filepath = os.path.join(root, file)
                relpath = os.path.relpath(filepath, path)
                with open(filepath, "rb") as f:
                    content = None
                    encoding = chardet.detect(f.read())['encoding']
                    f.seek(0)
                    try:
                        content = f.read().decode(encoding)
                    except UnicodeDecodeError:
                        print(f"File {os.path.join(prefix, relpath)} has an invalid encoding ({encoding}), falling back to {fallback_encoding}")
                        content = f.read().decode(fallback_encoding)
                print(f"## WRITE THIS FILE {os.path.join(prefix, relpath)}")
                print(content)

def print_directory_tree(path, prefix=''):
    for root, dirs, files in os.walk(path):
        # exclude hidden directories and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.startswith('.'):
                print(f"{sub_indent}{f}")

def print_dependency_graph(starting_script):
    import sys
    import ast
    from collections import defaultdict

    sys.path.append(os.path.abspath(os.path.dirname(starting_script)))

    visited = set()
    queue = deque([starting_script])
    graph = defaultdict(set)

    while queue:
        script = queue.popleft()
        if script not in visited:
            visited.add(script)

            spec = importlib.util.spec_from_file_location(Path(script).stem, script)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            with open(script, 'rt') as file:
                tree = ast.parse(file.read(), script)

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        graph[module.__name__].add(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module is not None:
                        graph[module.__name__].add(node.module)

    for key, values in graph.items():
        print(f"{key}:")
        for value in values:
            print(f"    {value}")

def main():
    print("```")
    print("# CONTENT:")
    send_directory(".")
    print("# NO MORE FILES FROM CHATGPT")
    print("```")

    print("\nDirectory Tree:")
    print_directory_tree(".")

    starting_script = "./src/mvp_cli.py"
    print(f"\nDependency Graph for {starting_script}:")
    print_dependency_graph(starting_script)

if __name__ == "__main__":
    main()

