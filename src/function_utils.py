import ast
import inspect

def get_functions_from_ast(module_ast):
    functions = []
    for node in ast.walk(module_ast):
        if isinstance(node, ast.FunctionDef):
            functions.append(node)
    return functions

def get_function_signature(func_def):
    arg_names = [arg.arg for arg in func_def.args.args]
    signature = f"{func_def.name}({', '.join(arg_names)})"
    return signature

def get_module_functions(module):
    functions = []
    for name in dir(module):
        obj = getattr(module, name)
        if inspect.isfunction(obj) and obj.__module__ == module.__name__:
            functions.append(obj)
    return functions

def process_functions(functions):
    functions.sort(key=lambda x: inspect.getsourcelines(x)[1])
    for func in functions:
        signature = get_function_signature(func)
        source_lines, starting_line_number = inspect.getsourcelines(func)
        ending_line_number = starting_line_number + len(source_lines) - 1
        print(f"  {signature} # LINES {starting_line_number}-{ending_line_number}")

