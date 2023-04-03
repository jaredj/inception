#!/usr/bin/env python3

import sys
from .directory_utils import process_directory_recursively

if __name__ == "__main__":
    if len(sys.argv) == 2:
        root_directory = sys.argv[1]
    else:
        root_directory = '.'

    process_directory_recursively(root_directory)