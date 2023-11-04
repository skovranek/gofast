"""Module providing the entry point main function to run the script."""
import os
#from subprocess import run

from .parse_cli_args import parse
from .load_yaml import load
from .write_file import write_file
from .go_mod import GO_MOD_CONTENTS
from .go_main import GO_MAIN_CONTENTS
from .go_create_server import GO_CREATE_SERVER_CONTENTS


def main():
    """Function starts the script."""
    args = parse()
    data = load(args.yaml)
    root = args.dir

    # for dev, remove later
    #run('rm -rf ~/work/gofast/out', shell=True, check=True)
    #run('rm -rf ~/work/gofast/output', shell=True, check=True)

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
    #run('go mod init replacethiswithmodulename', shell=True, check=True)
    #run('go get github.com/go-chi/chi/v5', shell=True, check=True)
    #run('go get github.com/go-chi/cors', shell=True, check=True)

    write_file('main.go', GO_MAIN_CONTENTS)
    write_file('go.mod', GO_MOD_CONTENTS.format(args.mod))
    write_file('create_server.go', GO_CREATE_SERVER_CONTENTS)

    if args.execute:
        print('Building and executing Go module')
        #run('go build -o out && ./out', shell=True, check=True)
    elif args.build:
        print('Building Go module')
        #run('go build -o out', shell=True, check=True)

    print('Done')


if __name__ == "__main__":
    main()
