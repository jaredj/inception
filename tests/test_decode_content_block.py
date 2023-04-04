import os
import shutil
import tempfile
import unittest

from inception.decode.file_parser import parse_content_block
from inception.decode.file_writer import write_files

class TestDecodeContentBlock(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

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
