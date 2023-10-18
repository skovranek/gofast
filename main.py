#!/usr/bin/env python

import argparse
import subprocess
import sys
from ruamel.yaml import YAML

def main():
    parser = argparse.ArgumentParser(description="Generate an API and/or static server in Go according to an OpenAPI spec in a YAML file.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("yaml_file", help="The YAML file containing the OpenAPI spec.")
    parser.add_argument("destination", help="The location of the directory in which to generate your Go module.")
    args = parser.parse_args()

    with open(args.yaml_file, 'r') as yaml_data:
        try:
            yaml=YAML(typ="safe", pure=True)
            data = yaml.load(yaml_data)
        except yaml.YAMLError as e:
            print(f"YAML parsing error: {e}")

    dir = args.destination

    #subprocess.run(f"mkdir {dir}", shell=True)

    with open(f'{dir}/output.txt', 'a') as f:
        f.write(data['key'])

if __name__ == "__main__":
    main()
