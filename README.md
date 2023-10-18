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
echo 'export PATH=$PATH:$HOME/path/to/gofast' >> ~/.zshrc
```
or symlink it to the './venv/bin/' directory
```
$ ln -s gofast ./venv/bin/gofast
```

4) The new 'gofast' command takes two arguments. First, the YAML file. Second, the destination directory for the 'output.txt' file. Run GoFast: 
```
$ gofast data.yml output.txt
```
