from typing import Dict

import argparse

def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='GoFast',
        description="Generate an API and/or static server in Go according to an OpenAPI spec in a YAML file.",
        epilog='Created by Matt Skovranek'
    )

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display detailed processing information"
    )
    verbosity.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="display minimal information"
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
        help="execute the Go binary"
    )

    parser.add_argument(
        "yaml_file",
        help="the YAML file containing the OpenAPI spec",
    )
    parser.add_argument(
        "destination",
        help="the location of the directory in which to generate your Go module",
    )

    return parser.parse_args()
