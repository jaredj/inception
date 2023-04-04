import os
import shutil
import tempfile
import unittest

from inception.introspect.send_files.send_file_or_directory import send_file_or_directory
from inception.decode.file_parser import parse_content_block

class TestSendDirectory(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

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

if __name__ == '__main__':
    unittest.main()
