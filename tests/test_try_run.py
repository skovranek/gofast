"""Module testing running subprocess on shell in a try block."""
import unittest
from unittest.mock import patch  # Mock

from gofast.try_run import try_run


class TestTryRun(unittest.TestCase):
    """Class testing run function from 'try_run.py'."""

    @patch('subprocess.run')
    def test_try_run_echo(self, mock):
        """Method mocks echo command."""
        # mock.return_value = Mock(stdout="go version go1.21.0")
        self.assertTrue(try_run('echo hello'))

    @patch('subprocess.run')
    def test_try_run_not_found(self, mock):
        """Method mocks nonexistent command."""
        # mock.return_value = Mock(stdout="zsh: command not found: hello")
        self.assertFalse(try_run('hello'))

    @patch('subprocess.run')
    def test_try_run_exception(self, mock):
        """Method mocks an exception."""
        # mock.side_effect = Exception("mock error")
        self.assertFalse(try_run('hello'))


if __name__ == '__main__':
    unittest.main()
