import sys
import os
import importlib.util
from .function_utils import get_module_functions, process_functions

def print_file_function_signatures(filepath):
    print(f"File: {filepath}")

    module_name = os.path.splitext(os.path.basename(filepath))[0]

    current_directory = os.path.abspath(os.path.dirname(filepath))
    sys.path.insert(0, current_directory)

    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    functions = get_module_functions(module)
    process_functions(functions)

    sys.path.remove(current_directory)
