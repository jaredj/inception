import unittest
from unittest.mock import MagicMock, patch
from inception.git.integrate_git import (
    get_current_branch_name,
    create_and_checkout_inception_branch,
    integrate_git_operations,
)

class TestIntegrateGitOperations(unittest.TestCase):
    @patch("inception.git.integrate_git.Repo")
    def test_get_current_branch_name(self, mock_repo):
        mock_repo.active_branch.name = "main"
        branch_name = get_current_branch_name()
        self.assertEqual(branch_name, "main")

    @patch("inception.git.integrate_git.Repo")
    def test_create_and_checkout_inception_branch(self, mock_repo):
        branch_name = create_and_checkout_inception_branch("test commit")
        self.assertTrue(branch_name.startswith("incept-test-commit"))
        mock_repo.git.checkout.assert_called_once_with("-b", branch_name)

    @patch("inception.git.integrate_git.Repo")
    def test_integrate_git_operations(self, mock_repo):
        git_add = MagicMock()
        git_commit = MagicMock(return_value=["test_file.py"])
        with patch("inception.git.integrate_git.git_add", git_add):
            with patch("inception.git.integrate_git.git_commit", git_commit):
                files_changed = integrate_git_operations("test_file.py", "test commit")
                git_add.assert_called_once_with(mock_repo, "test_file.py")
                git_commit.assert_called_once_with(mock_repo, "test commit")
                self.assertEqual(files_changed, ["test_file.py"])

