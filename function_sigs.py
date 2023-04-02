#!/usr/bin/env python3

import os
import sys
import inspect
import importlib.util

# Add the 'src' directory to the Python path
src_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.insert(0, src_directory)

# Import the required function
from signature_utils import print_file_function_signatures

def process_directory_recursively(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                print_file_function_signatures(filepath)

if __name__ == "__main__":
    root_directory = os.path.dirname(os.path.abspath(__file__))
    process_directory_recursively(root_directory)

