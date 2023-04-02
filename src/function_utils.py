import inspect

def get_function_signature(fn):
    sig = inspect.signature(fn)
    return f"{fn.__name__}{sig}"

def get_module_functions(module):
    functions = []
    for name in dir(module):
        obj = getattr(module, name)

        if inspect.isfunction(obj):
            functions.append(obj)
        elif inspect.isclass(obj):
            for method_name in dir(obj):
                method = getattr(obj, method_name)
                if inspect.isfunction(method):
                    functions.append(method)
    return functions

def process_functions(functions):
    functions.sort(key=lambda x: inspect.getsourcelines(x)[1])
    for func in functions:
        signature = get_function_signature(func)
        source_lines, starting_line_number = inspect.getsourcelines(func)
        ending_line_number = starting_line_number + len(source_lines) - 1
        print(f"  {signature} # LINES {starting_line_number}-{ending_line_number}")

