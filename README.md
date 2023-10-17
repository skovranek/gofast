# GoFast
A python project to generate go APIs.

## How to Execute GoFast
> **Note**
> This is just an intermediate stage, for proof of concept.

[How to create a CLI Cmd](https://dbader.org/blog/how-to-make-command-line-commands-with-python)
1) Rename 'main.py' to 'gofast':
```
$ mv main.py gofast
```

2) Make sure 'gofast' has executable permission. 
```
$ chmod +x gofast
```

3) Add GoFast to your PATH. If on a mac with Zsh, add something like this line to '.zshrc':
```
export PATH=$PATH:$HOME/path/to/gofast
```

4) The new 'gofast' command takes two arguments. First, the YAML file. Second, the destination file for the output. Run GoFast: 
```
$ gofast data.yml output.txt
```
