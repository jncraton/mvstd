mvstd
=====

[![PyPI version](https://badge.fury.io/py/mvstd.svg)](https://badge.fury.io/py/mvstd)
[![Build](https://github.com/jncraton/mvstd/actions/workflows/build.yml/badge.svg)](https://github.com/jncraton/mvstd/actions/workflows/build.yml)

Renames a file using a standard format

Installation
------------

The program can be installed using pip:

```
pip3 install mvstd
```

Usage
-----

```
usage: mvstd.py [-h] [--numeric] [--reverse] [--scene] files [files ...]

Rename files to a standard format

positional arguments:
  files          List of files

optional arguments:
  -h, --help     show this help message and exit
  --numeric, -n  Rename file numerically after sorting alphabetically
  --reverse, -r  Reverse sort order prior to renaming
  --scene, -s    Rename using scene rules
```
