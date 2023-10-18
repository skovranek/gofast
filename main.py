#!/usr/bin/env python

import argparse
import os
import subprocess
import sys
from ruamel.yaml import YAML

def main():
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
        "yaml_file",
        help="the YAML file containing the OpenAPI spec",
    )
    parser.add_argument(
        "destination",
        help="the location of the directory in which to generate your Go module",
    )
    args = parser.parse_args()

    with open(args.yaml_file, 'r') as yaml_data:
        try:
            yaml=YAML(typ="safe", pure=True)
            data = yaml.load(yaml_data)
        except yaml.YAMLError as e:
            print(f"YAML parsing error: {e}")

    dir = args.destination

    os.chdir(dir)
    subprocess.run(f"go mod init {data['path']}", shell=True)

    with open(f'output.txt', 'a') as f:
        f.write(data['key'])

    if args.quiet:
        print("done")
    elif args.verbose:
        print(f"Writing '{data['key']}' to '{dir}/output.txt'")
    else:
        print(f"Writing to '{dir}/output.txt'")

if __name__ == "__main__":
    main()
