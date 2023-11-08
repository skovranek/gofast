"""Module testing checking go version."""
from unittest import TestCase
from unittest.mock import patch, Mock

from gofast.check_go_version import go1_21

class TestCheckGoVersion(TestCase):
    """Class testing go version function from 'check_go_version.py'."""
    @patch('subprocess.run')
    def test_go1_21(self, mock):
        """Method mocks Go version go1.21.0."""
        mock.return_value = Mock(stdout="go version go1.21.0")
        self.assertTrue(go1_21())

    @patch('subprocess.run')
    def test_go1_22(self, mock):
        """Method mocks a Go version later than go1.21.0."""
        mock.return_value = Mock(stdout="go version go1.22.0")
        self.assertTrue(go1_21())

    @patch("subprocess.run")
    def test_go1_20(self, mock):
        """Method mocks a Go version earlier than go1.21.0."""
        mock.return_value = Mock(stdout="go version go1.20.0")
        self.assertFalse(go1_21())

    @patch('subprocess.run')
    def test_go_not_installed(self, mock):
        """Method mocks Go not being installed."""
        mock.return_value = Mock(stdout="zsh: command not found: go")
        self.assertFalse(go1_21())

    @patch('subprocess.run')
    def test_exception(self, mock):
        """Method mocks an exception."""
        mock.side_effect = Exception("mock error")
        self.assertFalse(go1_21())


if __name__ == '__main__':
    unittest.main()
