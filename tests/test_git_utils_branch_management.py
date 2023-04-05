import unittest
from unittest.mock import MagicMock, patch
from inception.git.git_utils import (
    create_branch,
    checkout_branch,
    merge_branch,
    delete_branch,
)

class TestGitUtilsBranchManagement(unittest.TestCase):
    @patch("inception.git.git_utils.Repo")
    def test_create_branch(self, mock_repo):
        create_branch(mock_repo, "test_branch")
        mock_repo.git.checkout.assert_called_once_with("-b", "test_branch")

    @patch("inception.git.git_utils.Repo")
    def test_checkout_branch(self, mock_repo):
        checkout_branch(mock_repo, "test_branch")
        mock_repo.git.checkout.assert_called_once_with("test_branch")

    @patch("inception.git.git_utils.Repo")
    def test_merge_branch(self, mock_repo):
        merge_branch(mock_repo, "source_branch", "target_branch")
        mock_repo.git.checkout.assert_called_once_with("target_branch")
        mock_repo.git.merge.assert_called_once_with("source_branch", "--no-ff", "--no-commit")

    @patch("inception.git.git_utils.Repo")
    def test_delete_branch(self, mock_repo):
        delete_branch(mock_repo, "test_branch")
        mock_repo.git.branch.assert_called_once_with("-D", "test_branch")
