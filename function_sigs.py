#!/usr/bin/env python3

import os
import sys
import inspect
import importlib.util


def get_function_signature(fn):
    sig = inspect.signature(fn)
    return f"{fn.__name__}{sig}"


def process_directory_recursively(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                print(f"File: {filepath}")

                module_name = os.path.splitext(filename)[0]

                # Add the current directory to the Python path for imports
                current_directory = os.path.abspath(dirpath)
                sys.path.insert(0, current_directory)

                spec = importlib.util.spec_from_file_location(module_name, filepath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                functions = []
                for name in dir(module):
                    obj = getattr(module, name)

                    if inspect.isfunction(obj):
                        functions.append(obj)

                functions.sort(key=lambda x: inspect.getsourcelines(x)[1])

                for func in functions:
                    signature = get_function_signature(func)
                    source_lines, starting_line_number = inspect.getsourcelines(func)
                    ending_line_number = starting_line_number + len(source_lines) - 1
                    print(f"  {signature} # LINES {starting_line_number}-{ending_line_number}")

                # Remove the current directory from the Python path
                sys.path.remove(current_directory)


if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))
    process_directory_recursively(root_directory)

