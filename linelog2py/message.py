# Author: Yuji Sasaki <yuji@sasaki.dev>
# Copyright (c) 2022 Yuji Sasaki
# License: MIT License

from datetime import datetime

from .category import Category

class Message:

  time: datetime
  username: str
  textlines: list[str]
  kind: Category

  def __init__(self, _datetime: datetime, _username: str, _text: list, _kind: Category = Category.TEXT):
    self.time = _datetime
    self.username = _username
    self.textlines = [_text]
    self.kind = _kind

  def addMessage(self, text: str) -> None:
    self.textlines.append(text)

  def asList(self) -> list[str]:
    return [self.time, self.username, " ".join(self.textlines)]

  def __str__(self):
    return f'{self.time}, {self.username}, "{" ".join(self.textlines)}"'