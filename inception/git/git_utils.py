from git import Repo

def create_branch(repo, branch_name):
    repo.git.checkout('-b', branch_name)

def checkout_branch(repo, branch_name):
    repo.git.checkout(branch_name)

def merge_branch(repo, source_branch, target_branch):
    repo.git.checkout(target_branch)
    repo.git.merge(source_branch, '--no-ff', '--no-commit')

def delete_branch(repo, branch_name):
    repo.git.branch('-D', branch_name)

def git_diff(repo, file_path):
    diff = repo.git.diff(None, file_path)
    return diff

def git_diffstat(repo):
    diffstat = repo.git.diff(None, '--stat')
    return diffstat

def git_add(repo, file_path):
    repo.git.add(file_path)

def git_commit(repo, commit_message):
    repo.git.commit('-m', commit_message)

def git_squash(repo, start_commit, end_commit, new_message):
    repo.git.rebase('-i', f"{start_commit}^{end_commit}", input=f"r {start_commit} {new_message}\n")

def get_branch_difference(repo, branch_name):
    parent_branch = repo.git.merge_base("main", branch_name)
    return repo.git.diff(parent_branch, branch_name)

def perform_git_operations(repo, file_path, commit_message, start_commit=None, end_commit=None, new_message=None):
    diff = git_diff(repo, file_path)
    if diff:
        git_add(repo, file_path)
        git_commit(repo, commit_message)

        if start_commit and end_commit and new_message:
            git_squash(repo, start_commit, end_commit, new_message)
        return True
    else:
        return False