#!/usr/bin/env python3
import inspect
import os
import sys
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

def find_imports(module):
    imports = []
    for name, obj in inspect.getmembers(module):
        if inspect.ismodule(obj):
            imports.append(obj.__name__)
    return imports

def print_dependency_graph(starting_script):
    visited = set()
    queue = deque([starting_script])

    while queue:
        module_path = queue.popleft()
        module_name = os.path.splitext(os.path.basename(module_path))[0]

        if module_name not in visited:
            visited.add(module_name)
            spec = importlib.util.spec_from_file_location(module_name, module_path)

            if spec is not None:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                print(f"{module_name}:")
                
                if hasattr(module, "__path__"):
                    search_path = module.__path__
                else:
                    search_path = None

                for imp in find_imports(module):
                    print(f"    {imp}")
                    imp_path = find_module_path(imp, search_path)
                    if imp_path is not None:
                        queue.append(imp_path)

def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
    print("```")
    print("# CONTENT:")
    send_directory(".")
    print("# NO MORE FILES FROM CHATGPT")
    print("```")

    print("Directory Tree:")
    print_directory_tree(".")

    starting_script = os.path.join(os.path.dirname(__file__), "src", "mvp_cli.py")
    print("\nDependency Graph for ./src/mvp_cli.py:")
    print_dependency_graph(starting_script)


if __name__ == "__main__":
    main()

