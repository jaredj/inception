#!/usr/bin/env python3

import os
import inspect
import importlib.util

# Define a function to get the signature of a function
def get_function_signature(fn):
    sig = inspect.signature(fn)
    return f"{fn.__name__}{sig}"

# Loop through all the files in the current directory
for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        # Only process .py files
        if filename.endswith(".py"):
            filepath = os.path.join(dirpath, filename)
            print(f"File: {filepath}")

            # Load the module
            module_name = filename[:-3]  # Strip off the .py extension
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Loop through all the objects in the module
            functions = []
            for name in dir(module):
                obj = getattr(module, name)

                # Only process functions
                if inspect.isfunction(obj):
                    functions.append(obj)

            # Sort the functions by their starting line number
            functions.sort(key=lambda x: inspect.getsourcelines(x)[1])

            # Print the functions in order
            for func in functions:
                print(f"Function: {func.__name__}")
                print(f"  Signature: {get_function_signature(func)}")

                # Get the start and end line numbers for the function
                source_lines, starting_line_number = inspect.getsourcelines(func)
                ending_line_number = starting_line_number + len(source_lines) - 1
                print(f"  Defined at line {starting_line_number} to {ending_line_number}")

