import os
import shutil
import tempfile
import unittest

from inception.introspect.functions.function_sigs import process_directory_recursively
from inception.introspect.send_files.send_file_or_directory import send_file_or_directory
from inception.decode.file_parser import parse_content_block

class TestFunctionSigs(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_function_sigs(self):
        test_dir_path = os.path.join(self.test_dir, "test_dir")
        os.mkdir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, "test_file.py")
        test_file_contents = "def test_function():\n    pass\n"
        with open(test_file_path, "w") as f:
            f.write(test_file_contents)
        process_directory_recursively(test_dir_path)
        content_block = send_file_or_directory(os.path.join(test_dir_path, "function_sigs.txt"))
        parsed_content_block = parse_content_block(content_block)
        self.assertIn(test_file_path, parsed_content_block.keys())
        self.assertIn("test_function", parsed_content_block[test_file_path])

if __name__ == '__main__':
    unittest.main()
