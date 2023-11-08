"""Module testing replacing a line in a file."""
import unittest
from unittest.mock import mock_open, patch

from gofast.replace_line import replace_line

class TestReplaceLine(unittest.TestCase):
    """Class testing replace_line function from 'gofast/replace_line.py'."""

    def test_replace_line(self):
        """Method tests replacing one line of a file."""
        actual = replace_line('tests/mock_data.txt', 0, 'new_line\n')
        self.assertTrue(actual)

    def test_replace_line_undo(self):
        """Method resets test file."""
        actual = replace_line('tests/mock_data.txt', 0, 'line0\n')
        self.assertTrue(actual)

    def test_empty_file(self):
        """Method expects false from passing an empty file."""
        actual = replace_line(
            'tests/empty_file_for_testing.txt',
            0,
            'new_line'
        )
        self.assertFalse(actual)

    def test_no_file(self):
        """Method expects false from passing nonexistent file."""
        actual = replace_line(
            'tests/file_does_not_exist.txt',
            0,
            'new_line'
        )
        self.assertFalse(actual)

    def test_no_line(self):
        """Method expects false from trying a nonexistent line number."""
        actual = replace_line('tests/mock_data.txt', 2, 'new_line')
        self.assertFalse(actual)

    def test_negative_line(self):
        """Method expects false from trying a nonexistent line number."""
        actual = replace_line('tests/mock_data.txt', -1, 'new_line')
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
