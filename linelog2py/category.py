# Author: Yuji Sasaki <yuji@sasaki.dev>
# Copyright (c) 2022 Yuji Sasaki
# License: MIT License

from enum import Enum

class Category(Enum):
  NONE = 0
  TEXT = 1
  IMAGE = 2
  MOVIE = 3
  STAMP = 4
  FILE = 5
  CALL = 6
  CALL_CANCELLED = 7
  CALL_MISSED = 8
  CONTACT = 9
  UNSENT = 10
  POLL = 11

  @classmethod
  def fromLabel(cls, label: str):
    if label == '[写真]' or label == '[Photo]':
      return cls.IMAGE
    elif label == '[動画]' or label == '[Video]':
      return cls.MOVIE
    elif label == '[ファイル]' or label == '[File]':
      return cls.FILE
    elif label == '[スタンプ]' or label == '[Sticker]':
      return cls.STAMP
    elif label == '[連絡先]' or label == '[Contact]':
      return cls.CONTACT
    elif label == '[投票]' or label == '[Poll]':
      return cls.POLL
    else:
      return cls.NONE
    
