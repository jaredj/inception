import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from inception.git.integrate_git import (
    get_current_branch_name,
    create_and_checkout_inception_branch,
    integrate_git_operations,
)

class TestIntegrateGitOperations(unittest.TestCase):
    @patch("inception.git.integrate_git.Repo")
    def test_get_current_branch_name(self, mock_repo):
        mock_branch = MagicMock()
        type(mock_branch).name = PropertyMock(return_value="test_branch")
        mock_repo.return_value.active_branch = mock_branch
        result = get_current_branch_name()
        self.assertEqual(result, "test_branch")
        self.assertEqual(mock_repo.return_value.active_branch.name, "test_branch")

    @patch("inception.git.integrate_git.Repo")
    def test_create_and_checkout_inception_branch(self, mock_repo):
        mock_repo.return_value.git.checkout.return_value = None
        branch_name = create_and_checkout_inception_branch("test commit")
        self.assertTrue(branch_name.startswith("incept-test-commit"))
        mock_repo.return_value.git.checkout.assert_called_once_with("-b", branch_name)

    @patch("inception.git.integrate_git.Repo")
    def test_integrate_git_operations(self, mock_repo):
        mock_repo.return_value.git.add.return_value = None
        mock_repo.return_value.git.commit.return_value = None
        integrate_git_operations("test_file_path", "test commit message")
        mock_repo.return_value.git.add.assert_called_once_with("test_file_path")
        mock_repo.return_value.git.commit.assert_called_once_with("-m", "test commit message")

