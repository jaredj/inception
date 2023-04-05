import unittest
from unittest.mock import MagicMock, patch
from inception.git.git_utils import (
    git_diff,
    git_diffstat,
    git_add,
    git_commit,
    perform_git_operations,
)

class TestGitUtilsOperations(unittest.TestCase):
    @patch("inception.git.git_utils.Repo")
    def test_git_diff(self, mock_repo):
        git_diff(mock_repo, "test_file.py")
        mock_repo.git.diff.assert_called_once_with(None, "test_file.py")

    @patch("inception.git.git_utils.Repo")
    def test_git_diffstat(self, mock_repo):
        git_diffstat(mock_repo)
        mock_repo.git.diff.assert_called_once_with(None, "--stat")

    @patch("inception.git.git_utils.Repo")
    def test_git_add(self, mock_repo):
        git_add(mock_repo, "test_file.py")
        mock_repo.git.add.assert_called_once_with("test_file.py")

    @patch("inception.git.git_utils.Repo")
    def test_git_commit(self, mock_repo):
        git_commit(mock_repo, "test commit")
        mock_repo.git.commit.assert_called_once_with("-m", "test commit")

    @patch("inception.git.git_utils.Repo")
    def test_perform_git_operations(self, mock_repo):
        diff = MagicMock(return_value=True)
        add = MagicMock()
        commit = MagicMock()
        with patch("inception.git.git_utils.git_diff", diff):
            with patch("inception.git.git_utils.git_add", add):
                with patch("inception.git.git_utils.git_commit", commit):
                    success = perform_git_operations(mock_repo, "test_file.py", "test commit")
                    diff.assert_called_once_with(mock_repo, "test_file.py")
                    add.assert_called_once_with(mock_repo, "test_file.py")
                    commit.assert_called_once_with(mock_repo, "test commit")
                    self.assertTrue(success)

