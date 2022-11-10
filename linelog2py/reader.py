# Author: Yuji Sasaki <yuji@sasaki.dev>
# Copyright (c) 2022 Yuji Sasaki
# License: MIT License

from datetime import datetime
from itertools import groupby
import re

from .message import Message
from .category import Category

class Reader:

  def readFile(file: str) -> list[Message]:
    lines = []
    with open(file) as f:
      lines = f.readlines()[2:]

    dateString = "2020/01/01"
    isNextNewDate = False

    messages: list[Message] = []


    for line in lines:
      if line == '\n':
        isNextNewDate = True
        continue
      
      if isNextNewDate and re.match('\d{4}/\d{2}/\d{2}', line):
        dateString = line[:10].replace('\n', '')
        isNextNewDate = False
        continue

      splitted = line.split('\t')

      if len(splitted) == 3:
        time = datetime.strptime(f'{dateString} {splitted[0]}', '%Y/%m/%d %H:%M')
        text = splitted[2].replace('"','').replace('\n', '')

        if text.startswith("[") and text.endswith("]"):
          messages.append(
            Message(time, splitted[1], '', Category.fromLabel(text))
          )
        else:
          if text.startswith("☎ 通話時間"):
            messages.append(Message(time, splitted[1], text, Category.CALL))
          elif text.startswith("☎ 通話をキャンセルしました"):
            messages.append(Message(time, splitted[1], text, Category.CALL_CANCELLED))
          elif text.startswith("☎ 不在着信"):
            messages.append(Message(time, splitted[1], text, Category.CALL_MISSED))
          else:
            messages.append(Message(time, splitted[1], text))
      else:
        messages[-1].addMessage(line.replace('"', '').replace('\n', ''))
      
    return messages