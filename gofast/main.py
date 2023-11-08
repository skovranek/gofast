"""Module providing the entry point main function to run the script."""
from os import path, makedirs, chdir
from sys import exit as sysexit
from shlex import quote

from .check_go_version import go_1_21
from .parse_cli_args import parse
from .load_yaml import load
from .write_file import write_file
from .replace_line import replace_line
from .try_run import try_run

from .go_mod import GO_MOD_CONTENTS
from .go_main import GO_MAIN_CONTENTS
from .go_create_server import GO_CREATE_SERVER_CONTENTS


def main():
    """Function starts the script."""
    if not go_1_21():
        return

    args = parse()
    data = load(args.yaml)
    root = args.dir

    # for dev, remove later
    print('(dev: removing "output" directory)')
    try_run(f'rm -rf ~/work/gofast/out') or sysexit()
    try_run('rm -rf ~/work/gofast/output') or sysexit()

    if not path.exists(root):
        print(f"Making '{root}' directory")
        makedirs(root)

    chdir(root)

    if args.quiet:
        print('Initializing')
    elif args.verbose:
        print(f"Initializing '{data['info']['title']}' in '{root}'")
    else:
        print(f"Initializing Go module in '{root}'")

    try_run(f'go mod init {quote(args.mod)}') or sysexit()

    # install Go dependencies
    try_run('go get github.com/go-chi/chi/v5') or sysexit()
    try_run('go get github.com/go-chi/cors') or sysexit()

    #write_file('go.mod', GO_MOD_CONTENTS.format(args.mod))
    write_file('main.go', GO_MAIN_CONTENTS)
    write_file('create_server.go', GO_CREATE_SERVER_CONTENTS)

    # lint Go
    print('Linting Go module')
    try_run('go fmt ./...') or sysexit()

    # if test or build or execute
    if args.test or args.build or args.execute:
        print('Testing Go module')
        try_run('go test -v ./...') or sysexit()

    # if only build
    if args.build:
        print('Building Go binary')
        try_run('go build -o out') or sysexit()

    # if both
    if args.build and args.execute:
        print('Executing Go binary')
        try_run('./out') or sysexit()

    # if only execute and not build
    if args.execute and not args.build:
        print('Running Go module')
        try_run('go run .') or sysexit()

    print('\ndone\n')

if __name__ == "__main__":
    main()
