# Author: Yuji Sasaki <yuji@sasaki.dev>
# Copyright (c) 2022 Yuji Sasaki
# License: MIT License

from datetime import datetime
from itertools import groupby
import re
from typing import List

from .message import Message
from .category import Category

class Reader:

  @classmethod
  def readFile(cls, file: str) -> list[Message]:
    lines = []
    with open(file) as f:
      lines = f.readlines()[2:]

    dateString = "2020/01/01"
    isNextNewDate = False
    messages: List[Message] = []

    for line in lines:
      if line == '\n':
        isNextNewDate = True
        continue
      
      if isNextNewDate and re.match('\d{4}/\d{2}/\d{2}', line):
        dateString = line[:10].replace('\n', '')
        isNextNewDate = False
        continue

      splitted = line.split('\t')

      if len(splitted) >= 3 and re.fullmatch(r'\d{2}:\d{2}', splitted[0]):
        time = datetime.strptime(f'{dateString} {splitted[0]}', '%Y/%m/%d %H:%M')
        messages.append(cls.makeMessafeFromLine(splitted, time))
      else:
        messages[-1].addMessage(line.replace('"', '').replace('\n', ''))
      
    return messages

  @classmethod
  def makeMessafeFromLine(cls, lineSplitted: List[str], time: str) -> Message:
    text = "".join(lineSplitted[2:]).replace('"','').replace('\n', '')
    if text.startswith("[") and text.endswith("]"):
      return Message(time, lineSplitted[1], text, Category.fromLabel(text))
    else:
      if text.startswith("[Poll]"):
        return Message(time, lineSplitted[1], text, Category.POLL)
      if text.startswith("☎ 通話時間") or text.startswith("☎ Call time"):
        return Message(time, lineSplitted[1], text, Category.CALL)
      elif text.startswith("☎ 通話をキャンセルしました") or text.startswith("☎ Canceled call"):
        return Message(time, lineSplitted[1], text, Category.CALL_CANCELLED)
      elif text.startswith("☎ 不在着信") or text.startswith("☎ No answer"):
        return Message(time, lineSplitted[1], text, Category.CALL_MISSED)
      elif lineSplitted[1] == "" and (text.endswith("unsent a message.") or text.endswith("メッセージの送信を取り消しました")):
        return Message(time, lineSplitted[1], text, Category.UNSENT)
      else:
        return Message(time, lineSplitted[1], text)
