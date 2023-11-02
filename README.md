# GoFast
A python project to generate go APIs.
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
## How to Execute GoFast
> **Note**
> This is just an intermediate stage, for proof of concept.


1) Create a virtual environment.
```
$ python3 -m venv venv
```

2) Start the virtual environment.
```
$ source venv/bin/activate
```

3) Make sure 'pip', 'setuptools' and 'wheel' are installed and up to date in the virtual environment.
```
python3 -m pip install --upgrade pip setuptools wheel
```

4) Install GoFast in the virtual environment.
```
$ python3 -m pip install -e .
```

4) The new 'gofast' command takes two arguments. First, the YAML file. Second, the destination directory for the Go module.
```
$ gofast data.yml output
```
