![Logo](https://github.com/scarrazza/vai/raw/master/extra/logo.png "Logo VAI")

# VAI
A simple tool to simplify shell operations when programming.

## Installation

Download the code and install using the setup script:

```Shell
$ python setup.py install
```

## Usage

Create a file and place the instructions in comments starting with the ``vai:`` tag, e.g. for latex compilation:

```Latex
% vai: pdflatex mydocument.tex
% vai: bibtex mydocument
% vai: pdflatex mydocument.tex
% vai: pdflatex mydocument.tex
\documentclass{article}
...
```

Then run ``vai``:

```Shell
$ vai
```

Check the examples folder in this git repository for more examples.
