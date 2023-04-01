#!/usr/bin/env python3
import os
import sys
from modulefinder import ModuleFinder

def print_dependency_graph(starting_script):
    finder = ModuleFinder()
    finder.run_script(starting_script)

    for name, mod in finder.modules.items():
        if not name.startswith("site") and not name.startswith("importlib"):
            print(f"{name}:")
            for dep in mod.globalnames.keys():
                if not dep.startswith("site") and not dep.startswith("importlib"):
                    print(f"    {dep}")

def main():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                starting_script = os.path.join(root, file)
                print(f"Dependency Graph for {starting_script}:")
                print_dependency_graph(starting_script)
                print()

if __name__ == "__main__":
    main()

