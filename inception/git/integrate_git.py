from git import Repo
from datetime import datetime
import os
from .utils import (
    stage_changes,
    commit_changes,
    get_diff_stats,
    get_branch_difference,
)

def get_current_branch_name():
    repo = Repo(search_parent_directories=True)
    return repo.active_branch.name

def create_and_checkout_inception_branch(commit_message):
    repo = Repo(search_parent_directories=True)
    if commit_message:
        branch_name = f"incept-{commit_message.lower().replace(' ', '-')}"
    else:
        branch_name = f"incept-{datetime.now().strftime('%Y-%m-%d-%H%M')}"
    repo.git.checkout("-b", branch_name)
    return branch_name

def print_diff_stats(files_changed, branch_name):
    repo = Repo(search_parent_directories=True)
    for file_path in files_changed:
        print(f"\nChanges in {file_path}:")
        print(get_diff_stats(repo, branch_name, file_path))

    if len(files_changed) > 1:
        print(f"\nChanges so far in {branch_name} branch:")
        print(get_branch_difference(repo, branch_name))

def print_merge_instructions(branch_name):
    print(f"\nTo squash and merge this branch into the parent branch, run:")
    print(f"git checkout main")
    print(f"git merge --squash {branch_name}")
    print(f"git commit -m 'Squash and merge {branch_name}'")
    print(f"git branch -d {branch_name}")

def integrate_git_operations(file_path, commit_message):
    repo = Repo(search_parent_directories=True)
    stage_changes(repo, file_path)
    files_changed = commit_changes(repo, commit_message)
    return files_changed
