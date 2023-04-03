#!/usr/bin/env python3

import ast
import os
import sys
import inspect
import importlib.util


# Add the 'src' directory to the Python path
src_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.insert(0, src_directory)

from function_utils import get_functions_from_ast, get_function_signature
from signature_utils import print_file_function_signatures

def process_directory_recursively(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                rel_filepath = os.path.relpath(filepath)
                print(f"File: {rel_filepath}")

                module_name = os.path.splitext(filename)[0]

                # Add the current directory to the Python path for imports
                current_directory = os.path.abspath(dirpath)
                sys.path.insert(0, current_directory)

                with open(filepath, 'r', encoding='utf-8') as file:
                    source_code = file.read()
                    module_ast = ast.parse(source_code, filepath)

                functions = get_functions_from_ast(module_ast)
                functions.sort(key=lambda x: x.lineno)

                for func in functions:
                    print(f"  {get_function_signature(func)} # LINES {func.lineno}-{func.end_lineno}")

                # Remove the current directory from the Python path
                sys.path.remove(current_directory)

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))
    process_directory_recursively(root_directory)

