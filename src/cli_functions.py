def handle_instruction():
    user_input = input("Provide an INSTRUCTION:\n")
    print_block("INSTRUCTION", user_input)

def handle_comment():
    user_input = input("Provide a COMMENT:\n")
    print_block("COMMENT", user_input)

def handle_skip():
    pass

def print_block(block_type, content):
    print("```\n# REMINDER")
    print_reminder()
    print("```\n")
    print(f"```\n#{block_type}\n{content}\n```\n")