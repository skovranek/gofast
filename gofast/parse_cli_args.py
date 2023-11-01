from typing import Dict

from argparse import Namespace, ArgumentParser

def parse() -> Namespace:
    parser = ArgumentParser(
        prog='GoFast',
        description="Generate an API Go module from an OpenAPI Description YAML file.",
        epilog='GoFast created by Matt Skovranek'
    )

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display process"
    )
    verbosity.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="display minimum detail"
    )

    parser.add_argument(
        "-b",
        "--build",
        action="store_true",
        help="build the Go binary"
    )
    # just for dev
    parser.add_argument(
        "-e",
        "--execute",
        action="store_true",
        help="build and execute the Go binary"
    )

    parser.add_argument(
        "yaml",
        help="the OpenAPI spec YAML file",
    )
    parser.add_argument(
        "dir",
        help="the directory in which to create the Go module",
    )
    parser.add_argument(
        "mod",
        help="the Go module name, usually a github repo",
    )

    return parser.parse_args()
