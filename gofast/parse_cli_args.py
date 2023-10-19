from typing import Dict

import argparse

def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='GoFast',
        description="Generate an API Go module from an OpenAPI spec YAML file.",
        epilog='Created by Matt Skovranek'
    )

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display detailed process"
    )
    verbosity.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="display minimal info"
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
        "yaml_file",
        help="the OpenAPI spec YAML file",
    )
    parser.add_argument(
        "destination",
        help="the directory of the API Go module",
    )

    return parser.parse_args()
