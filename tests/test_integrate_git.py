import unittest
from unittest.mock import MagicMock, patch
from inception.git.integrate_git import (
    get_current_branch_name,
    create_and_checkout_inception_branch,
    integrate_git_operations,
)

class TestIntegrateGit(unittest.TestCase):
    @patch("inception.git.integrate_git.Repo")
    def test_get_current_branch_name(self, mock_repo):
        mock_repo.return_value.active_branch.name = "main"
        branch_name = get_current_branch_name()
        self.assertEqual(branch_name, "main")

    @patch("inception.git.integrate_git.Repo")
    def test_create_and_checkout_inception_branch(self, mock_repo):
        branch_name = create_and_checkout_inception_branch("test branch")
        self.assertTrue(branch_name.startswith("incept-test-branch"))

    @patch("inception.git.integrate_git.Repo")
    def test_integrate_git_operations(self, mock_repo):
        stage_changes = MagicMock()
        commit_changes = MagicMock()
        with patch("inception.git.integrate_git.stage_changes", stage_changes):
            with patch("inception.git.integrate_git.commit_changes", commit_changes):
                integrate_git_operations("test_file.py", "test commit")
                stage_changes.assert_called_once_with(mock_repo.return_value, "test_file.py")
                commit_changes.assert_called_once_with(mock_repo.return_value, "test commit")
