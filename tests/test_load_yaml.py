import unittest
from unittest.mock import mock_open, patch

from gofast.load_yaml import load

yaml = """%YAML 1.2
---
openapi: 3.1.0
info:
  title: Test API
  version: 0.0.1
..."""

class TestLoadYaml(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=yaml)
    def test_load(self, mock):
        data = load('mock.yaml')
        
        mock.assert_called_once_with('mock.yaml', 'r')

        self.assertEqual(data['openapi'], '3.1.0')
        self.assertEqual(data['info']['title'], 'Test API')
        self.assertEqual(data['info']['version'], '0.0.1')

if __name__ == "__main__":
    unittest.main()
