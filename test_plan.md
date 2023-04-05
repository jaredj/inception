
# Test Plan for Interactive Git Workflow

This test plan describes a collection of step-by-step methods for manually verifying that the interactive Git workflow works as it should.

## Prerequisites

1. A Git repository with at least one commit.
2. The latest version of the interactive Git workflow script.

## Test Cases

### 1. Get the current branch name

**Steps:**

1. Run the script to get the current branch name.
2. Verify that the output matches the current branch name in the Git repository.

### 2. Create and checkout a new inception branch

**Steps:**

1. Run the script to create a new inception branch with a specific commit message.
2. Verify that the new branch is created with the correct name format: `incept-<commit_message>`.
3. Verify that the repository is checked out to the new inception branch.

### 3. Stage and commit changes

**Steps:**

1. Modify a file in the repository.
2. Run the script to stage and commit the changes with a specific commit message.
3. Verify that the changes are staged.
4. Verify that the changes are committed with the provided commit message.

### 4. Print diff stats

**Steps:**

1. Modify a file in the repository.
2. Stage and commit the changes.
3. Run the script to print the diff stats.
4. Verify that the diff stats are displayed correctly for the modified file.

### 5. Print merge instructions

**Steps:**

1. Run the script to print the merge instructions for the current inception branch.
2. Verify that the displayed instructions correctly describe the process to squash and merge the branch into the parent branch.
