import ast
import os
import sys
import importlib.util
from .function_utils import get_functions_from_ast, get_function_signature
from .signature_utils import print_file_function_signatures

def process_python_file(filepath, root_directory):
    relpath = os.path.relpath(filepath, root_directory)
    print(f"File: {relpath}")

    module_name = os.path.splitext(os.path.basename(filepath))[0]

    # Add the current directory to the Python path for imports
    current_directory = os.path.abspath(os.path.dirname(filepath))
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

def process_directory_recursively(root_directory='.'):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                process_python_file(filepath, root_directory)