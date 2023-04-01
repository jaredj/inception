#!/usr/bin/env python3

import os
import sys
from modulefinder import ModuleFinder

def print_dependency_graph(starting_script, internal_prefix):
    finder = ModuleFinder()
    finder.run_script(starting_script)

    internal_deps = set()
    external_deps = set()

    for name, mod in finder.modules.items():
        if not name.startswith("site") and not name.startswith("importlib"):
            for dep in mod.globalnames.keys():
                if not dep.startswith("site") and not dep.startswith("importlib"):
                    if dep.startswith(internal_prefix):
                        internal_deps.add(dep)
                    else:
                        external_deps.add(dep)

    print("Internal dependencies:")
    for dep in sorted(internal_deps):
        print(f"    {dep}")
    print("\nExternal dependencies:")
    for dep in sorted(external_deps):
        print(f"    {dep}")

def main():
    internal_prefix = "inception"  # Replace with your project name or internal module prefix

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                starting_script = os.path.join(root, file)
                print(f"Dependency Graph for {starting_script}:")
                print_dependency_graph(starting_script, internal_prefix)
                print()

if __name__ == "__main__":
    main()

