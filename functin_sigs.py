#!/usr/bin/env python3

import os
import inspect

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
            module = __import__(module_name)

            # Loop through all the objects in the module
            for name in dir(module):
                obj = getattr(module, name)

                # Only process functions
                if inspect.isfunction(obj):
                    print(f"Function: {name}")
                    print(f"  Signature: {get_function_signature(obj)}")
                    print(f"  Defined at line {inspect.getsourcelines(obj)[1]} to {inspect.getsourcelines(obj)[-1]}")

