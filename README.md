# GoFast
A python project to generate go APIs.

## How to Execute GoFast
> This is just an intermediate stage, for proof of concept.

[How to create a CLI Cmd](https://dbader.org/blog/how-to-make-command-line-commands-with-python)
1) Rename 'main.py' to 'gofast':
```
$ mv main.py gofast
```

1) Make sure 'gofast' is permitted to be executable:
```
$ chmod +x gofast
```

2) Add GoFast to your PATH. If on a mac with Zsh, add something like this line to '.zshrc':
```
export PATH=$PATH:$HOME/path/to/gofast
```

3) The new 'gofast' command takes two arguments. First, the YAML file. Second, the destination file for the output. Run GoFast: 
```
$ gofast data.yml output.txt
```
