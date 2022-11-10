from datetime import datetime

from category import Category

class Message:

  _datetime: datetime
  _username: str
  _textlines: list[str]
  _kind: Category

  def __init__(self, datetime: datetime, username: str, text: list, kind: Category = Category.TEXT):
    self._datetime = datetime
    self._username = username
    self._textlines = [text]
    self._kind = kind

  def addMessage(self, text: str) -> None:
    self._textlines.append(text)

  def asList(self) -> list[str]:
    return [self._datetime, self._username, " ".join(self._messages)]

  def __str__(self):
    return f'{self._datetime}, {self._username}, "{" ".join(self._messages)}"'