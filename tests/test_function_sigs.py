import os
import unittest
from inception.introspect.functions.directory_utils import process_directory_recursively

class TestFunctionSigs(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), "tmp")
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        test_dir_path = os.path.join(self.test_dir, "test_dir")
        if os.path.exists(test_dir_path):
            os.rmdir(test_dir_path)
        os.rmdir(self.test_dir)

    def test_function_sigs(self):
        test_dir_path = os.path.join(self.test_dir, "test_dir")
        os.makedirs(test_dir_path, exist_ok=True)

