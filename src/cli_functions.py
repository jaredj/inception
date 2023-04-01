import sys

def handle_instruction():
    print("Provide an INSTRUCTION:")
    return sys.stdin.readline().strip()

def handle_comment():
    print("Provide a COMMENT:")
    return sys.stdin.readline().strip()

def handle_skip():
    pass

