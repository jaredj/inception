
# Test Plan for Interactive Git Workflow

This test plan describes a collection of step-by-step methods for manually verifying that the interactive Git workflow works as it should.

## Prerequisites

1. A Git repository with at least one commit.
2. The latest version of the interactive Git workflow script.
3. A console entry point `integrate_git` added in the `setup.py` file.

## Test Cases

### 1. Get the current branch name

**Steps:**

1. Run the following command to get the current branch name:
   ```
   integrate_git current_branch
   ```
2. Verify that the output matches the current branch name in the Git repository by running `git branch`.

### 2. Create and checkout a new inception branch

**Steps:**

1. Run the following command to create a new inception branch with a specific commit message:
   ```
   integrate_git create_inception_branch "<commit_message>"
   ```
2. Verify that the new branch is created with the correct name format: `incept-<commit_message>` by running `git branch`.
3. Verify that the repository is checked out to the new inception branch by running `git branch`.

### 3. Stage and commit changes

**Steps:**

1. Modify a file in the repository.
2. Run the following command to stage and commit the changes with a specific commit message:
   ```
   integrate_git commit_changes "<file_path>" "<commit_message>"
   ```
3. Verify that the changes are staged by running `git diff --staged`.
4. Verify that the changes are committed with the provided commit message by running `git log`.

### 4. Print diff stats

**Steps:**

1. Modify a file in the repository.
2. Stage and commit the changes.
3. Run the following command to print the diff stats:
   ```
   integrate_git print_diff_stats "<branch_name>"
   ```
4. Verify that the diff stats are displayed correctly for the modified file by comparing with `git diff --stat <branch_name>`.

### 5. Print merge instructions

**Steps:**

1. Run the following command to print the merge instructions for the current inception branch:
   ```
   integrate_git print_merge_instructions "<branch_name>"
   ```
2. Verify that the displayed instructions correctly describe the process to squash and merge the branch into the parent branch.
