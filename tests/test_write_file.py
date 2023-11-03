"""Module testing writing to file."""
import unittest
from unittest.mock import mock_open, patch

from gofast.write_file import write_file


class TestWriteFile(unittest.TestCase):
    """Class testing write function from 'gofast/write_file.py'."""

    def test_write_file(self):
        """Method mocks writing file."""
        file_path = 'temp_testing_file.txt'
        contents = 'temporary file for testing write_file.py'

        m = mock_open()
        with patch('builtins.open', m):
            write_file(file_path, contents)
        m.assert_called_once_with(file_path, 'w', encoding='utf-8')
        m().write.assert_called_once_with(contents)


if __name__ == "__main__":
    unittest.main()
