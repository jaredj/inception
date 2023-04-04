import os
import shutil
import tempfile
import unittest

from inception.introspect.send_files.send_file_or_directory import send_file_or_directory
from inception.introspect.functions.function_sigs import process_directory_recursively
from inception.decode.file_parser import parse_content_block
from inception.decode.file_writer import write_files

class TestInception(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_send_file(self):
        test_file_path = os.path.join(self.test_dir, "test_file.txt")
        test_file_contents = "test file contents"
        with open(test_file_path, "w") as f:
            f.write(test_file_contents)
        content_block = send_file_or_directory(test_file_path)
        parsed_content_block = parse_content_block(content_block)
        self.assertEqual(parsed_content_block[test_file_path][0], test_file_contents)

    def test_send_directory(self):
        test_dir_path = os.path.join(self.test_dir, "test_dir")
        os.mkdir(test_dir_path)
        test_file_path = os.path.join(test_dir_path, "test_file.txt")
        test_file_contents = "test file contents"
        with open(test_file_path, "w") as f:
            f.write(test_file_contents)
        content_block = send_file_or_directory(test_dir_path)
        parsed_content_block = parse_content_block(content_block)
        self.assertEqual(parsed_content_block[test_file_path][0], test_file_contents)

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

    def test_decode_content_block(self):
        test_file_path = os.path.join(self.test_dir, "test_file.txt")
        test_file_contents = "test file contents"
        content_block = f"# CONTENT: Test\n## WRITE THIS FILE {test_file_path}\n{test_file_contents}\n# NO MORE FILES FROM CHATGPT"
        parsed_content_block = parse_content_block(content_block)
        write_files({os.path.join(self.test_dir, k): v for k, v in parsed_content_block.items()})
        with open(test_file_path, "r") as f:
            self.assertEqual(f.read(), test_file_contents)

if __name__ == '__main__':
    unittest.main()
