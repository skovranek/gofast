import unittest
from unittest.mock import patch

from gofast.parse_cli_args import parse


class TestParseCLIArgs(unittest.TestCase):
    def assert_parsed(self, expect, actual):
        for k, v in expect.items():
            self.assertIn(k, actual)
            self.assertEqual(getattr(actual, k), expect[k])

    def assert_system_exit_error(self, exception):
        self.assertIsInstance(exception, SystemExit)
        self.assertEqual(str(exception), '2')

    def test_no_args(self):
        with self.assertRaises(SystemExit) as context:
            parse()
        self.assert_system_exit_error(context.exception)
#        try:
#            parse()
#        except Exception as e:
#            self.fail(f"Exception: {str(e)}")

    @patch('sys.argv', [None, 'tests/openapi.yaml'])
    def test_one_arg_error(self):
        with self.assertRaises(SystemExit) as context:
            parse()
        self.assert_system_exit_error(context.exception)

    @patch('sys.argv', [None, 'tests/openapi.yaml', 'output'])
    def test_two_args_error(self):
        with self.assertRaises(SystemExit) as context:
            parse()
        self.assert_system_exit_error(context.exception)

    @patch('sys.argv', [
        None,
        'tests/openapi.yaml',
        'output',
        'github.com/skovranek/gofast'
    ])
    def test_yaml_dir_and_mod_args(self):
        expect = {
            'verbose': False,
            'quiet': False,
            'build': False,
            'execute': False,
            'yaml': 'tests/openapi.yaml',
            'dir': 'output',
            'mod': 'github.com/skovranek/gofast'
        }
        self.assert_parsed(expect, parse())

    @patch('sys.argv', [
        None,
        '--verbose',
        'tests/openapi.yaml',
        'output',
        'github.com/skovranek/gofast'
    ])
    def test_verbose_option(self):
        expect = {
            'verbose': True,
            'quiet': False,
            'build': False,
            'execute': False,
            'yaml': 'tests/openapi.yaml',
            'dir': 'output',
            'mod': 'github.com/skovranek/gofast'
        }
        self.assert_parsed(expect, parse())

    @patch('sys.argv', [
        None,
        '-v',
        'tests/openapi.yaml',
        'output',
        'github.com/skovranek/gofast'
    ])
    def test_v_flag(self):
        expect = {
            'verbose': True,
            'quiet': False,
            'build': False,
            'execute': False,
            'yaml': 'tests/openapi.yaml',
            'dir': 'output',
            'mod': 'github.com/skovranek/gofast'
        }
        self.assert_parsed(expect, parse())

    @patch('sys.argv', [
        None,
        '--verbose',
        '--quiet',
        'tests/openapi.yaml',
        'output',
        'github.com/skovranek/gofast'
    ])
    def test_verbose_and_quiet_options(self):
        with self.assertRaises(SystemExit) as context:
            parse()
        self.assert_system_exit_error(context.exception)

    @patch('sys.argv', [
        None,
        '--build',
        'tests/openapi.yaml',
        'output',
        'github.com/skovranek/gofast'
    ])
    def test_build_option(self):
        expect = {
            'verbose': False,
            'quiet': False,
            'build': True,
            'execute': False,
            'yaml': 'tests/openapi.yaml',
            'dir': 'output',
            'mod': 'github.com/skovranek/gofast'
        }
        self.assert_parsed(expect, parse())

    @patch('sys.argv', [
        None,
        '--execute',
        'tests/openapi.yaml',
        'output',
        'github.com/skovranek/gofast'
    ])
    def test_execute_option(self):
        expect = {
            'verbose': False,
            'quiet': False,
            'build': False,
            'execute': True,
            'yaml': 'tests/openapi.yaml',
            'dir': 'output',
            'mod': 'github.com/skovranek/gofast'
        }
        self.assert_parsed(expect, parse())

    @patch('sys.argv', [
        None,
        '-be',
        'tests/openapi.yaml',
        'output',
        'github.com/skovranek/gofast'
    ])
    def test_build_and_execute_flags(self):
        expect = {
            'verbose': False,
            'quiet': False,
            'build': True,
            'execute': True,
            'yaml': 'tests/openapi.yaml',
            'dir': 'output',
            'mod': 'github.com/skovranek/gofast'
        }
        self.assert_parsed(expect, parse())

    @patch('sys.argv', [
        None,
        '-qb',
        '--execute',
        'tests/openapi.yaml',
        'output',
        'github.com/skovranek/gofast'
    ])
    def test_quiet_and_build_flags_and_execute_option(self):
        expect = {
            'verbose': False,
            'quiet': True,
            'build': True,
            'execute': True,
            'yaml': 'tests/openapi.yaml',
            'dir': 'output',
            'mod': 'github.com/skovranek/gofast'
        }
        self.assert_parsed(expect, parse())


if __name__ == '__main__':
    unittest.main()
