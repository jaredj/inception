from .git_utils import perform_git_operations, git_diffstat
from git import Repo

def integrate_git_operations(file_path, commit_message, start_commit=None, end_commit=None, new_message=None):
    repo = Repo(search_parent_directories=True)
    file_changed = perform_git_operations(repo, file_path, commit_message, start_commit, end_commit, new_message)
    if file_changed:
        diffstat = git_diffstat(repo)
        print(f"Changes staged for {file_path}:\n{diffstat}\n")
    else:
        print(f"No changes detected for {file_path}\n")
