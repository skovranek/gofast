#!/usr/bin/env python

import os
import subprocess
import sys

from ruamel.yaml import YAML

from parse_cli_args import parse
from load_yaml import load

def main():
    args = parse()

    data = load(args.yaml_file)

    dir = args.destination

    if not os.path.exists(dir):
        if not args.quiet:
            print(f"'{dir}' directory not found. Creating directory.")
        os.makedirs(dir)

    os.chdir(dir)
    subprocess.run(f"go mod init {data['path']}", shell=True)

    with open(f'main.go', 'a') as f:
        f.write(f"package {data['package']}\n\n")
        f.write(f"import \"{data['import']}\"\n\n")
        f.write(f"func main() {{\n\tfmt.Println(\"hello world\")\n}}")

    if args.quiet:
        print("done")
    elif args.verbose:
        print(f"Writing '{data['package']}' to '{dir}/main.go'")
    else:
        print(f"Writing to '{dir}/main.go'")

    if args.execute:
        subprocess.run("go build -o out && ./out", shell=True)
    elif args.build:
        subprocess.run("go build -o out", shell=True)

if __name__ == "__main__":
    main()
