# linelog2py
[![PyPI](https://img.shields.io/pypi/v/PyGithub.svg)](https://pypi.python.org/pypi/linelog2py)

linelog2py is a library to import LINE Chat History to Python.

## Summary

This is a library to help you import LINE chat history files for text analysis, etc. It supports the input of a text file which can be output from the `LINE talk room settings screen` -> `Other Settings` -> `Export Chat History`. The language setting of LINE must be set to either English or Japanese when outputting the file.

## Installation

You can install it via PyPI.

```
# PyPI
$ pip install linelog2py
```

## Usage

Reading a file via `Reader` will output a list of `Message`.

```python
from linelog2py import *

file = './line_history.txt'

messages = Reader.readFile(file)

for message in messages:
  print(message)

```

## Documentation

### Message

#### Properties

`time: datetime`  Date and time the message was sent
`username: str` User's display name
`textlines: list[str]`  List of message sentences
`kind: Category`  Category of the message (Text, Sticker, etc.)

#### Methods

`def addMessage(self, text: str) -> None` Add line to the sentences list
`def asList(self) -> list[str]`  Output contents as list


### Category

#### Members

- NONE
- TEXT
- IMAGE
- MOVIE
- STAMP
- FILE
- CALL
- CALL_CANCELLED
- CALL_MISSED
- CONTACT
- UNSENT
- POLL

#### Methods

`def fromLabel(cls, label: str)`  Generate `Cateory` from label string.

### Reader

#### Methods

`def readFile(file: str) -> list[Message]` Read a file from the path and return a list of `Message`.

## Upload to PyPI

```
python3 setup.py bdist_wheel
python3 -m  twine upload --config-file ".pypirc" dist/*
```