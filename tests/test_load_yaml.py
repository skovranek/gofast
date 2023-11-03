"""Module providing testing for loading YAML data."""
import unittest
from unittest.mock import mock_open, patch

from gofast.load_yaml import load


CONTENT = """%YAML 1.2
---
openapi: 3.1.0
info:
  title: Test API
  version: 0.0.1
..."""

class TestLoadYaml(unittest.TestCase):
    """Class testing load function from 'gofast/load_yaml.py'."""

    @patch('builtins.open', new_callable=mock_open, read_data=CONTENT)
    def test_load(self, mock):
        """Method mocks yaml file to assert load outputs expected data."""
        data = load('mock.yaml')

        mock.assert_called_once_with('mock.yaml', 'r')

        self.assertEqual(data['openapi'], '3.1.0')
        self.assertEqual(data['info']['title'], 'Test API')
        self.assertEqual(data['info']['version'], '0.0.1')


if __name__ == "__main__":
    unittest.main()
