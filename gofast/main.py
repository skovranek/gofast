#!/usr/bin/env python

import os
from subprocess import run

from ruamel.yaml import YAML

from .parse_cli_args import parse
from .load_yaml import load

def main():
    args = parse()

    data = load(args.yaml_file)
    print(data)

    root = args.destination

    # for dev
    run(f"rm -rf ~/workspace/gofast/output", shell=True)

    if not os.path.exists(root):
        if not args.quiet:
            print(f"'{root}' directory not found. Creating directory.")
        os.makedirs(root)

    os.chdir(root)
    run(f"go mod init github.com/skovranek/repo", shell=True)

    with open(f'main.go', 'a') as f:
        f.write(f"package main\n\n")
        f.write(f"import \"fmt\"\n\n")
        f.write(f"func main() {{\n\tfmt.Println(\"hello world\")\n}}")

    if args.quiet:
        print("done")
    elif args.verbose:
        print(f"Writing '{data['info']['title']}' to '{root}/main.go'")
    else:
        print(f"Writing to '{root}/main.go'")

    if args.execute:
        run("go build -o out && ./out", shell=True)
    elif args.build:
        run("go build -o out", shell=True)

if __name__ == "__main__":
    main()
