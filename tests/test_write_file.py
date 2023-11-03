import unittest
from unittest.mock import mock_open, patch

from gofast.write_file import write_file


class TestWriteFile(unittest.TestCase):
    def test_write_file(self):
        file_path = 'temp_testing_file.txt'
        contents = 'temporary file for testing write_file.py'

        m = mock_open()
        with patch('builtins.open', m):
            write_file(file_path, contents)
        m.assert_called_once_with(file_path, 'w')
        m().write.assert_called_once_with(contents)


if __name__ == "__main__":
    unittest.main()
