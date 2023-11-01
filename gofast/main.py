import os
from subprocess import run

from ruamel.yaml import YAML

from .parse_cli_args import parse
from .load_yaml import load
from .write_file import write_file
from .go_create_server import contents

def main():
    args = parse()
    data = load(args.yaml)
    root = args.directory

    # for dev, remove later
    run('rm -rf ~/work/gofast/out', shell=True)
    run('rm -rf ~/work/gofast/output', shell=True)

    if not os.path.exists(root):
        print(f"Creating '{root}' directory")
        os.makedirs(root)

    if args.quiet:
        print('Initializing')
    elif args.verbose:
        print(f"Initializing '{data['info']['title']}' in '{root}'")
    else:
        print(f"Initializing Go module in '{root}'")

    os.chdir(root)
    run(f'go mod init {args.module}', shell=True)
    run('go get github.com/go-chi/chi/v5', shell=True)
    run('go get github.com/go-chi/cors', shell=True)

    main_go = """package main

import (
    "fmt"
    "log"
)

func main() {
    fmt.Println("hello world")

	srv := createServer()

	log.Print("Starting server on port #8000")
	log.Fatal(srv.ListenAndServe())
}"""

    write_file('main.go', main_go)

    write_file('create_server.go', contents)

    if args.execute:
        print('Building and executing Go module')
        run('go build -o out && ./out', shell=True)
    elif args.build:
        print('Building Go module')
        run('go build -o out', shell=True)
    
    print('Done')

if __name__ == "__main__":
    main()
