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

  @classmethod
  def fromLabel(cls, label: str):
    if label == '[写真]':
      return cls.IMAGE
    elif label == '[動画]':
      return cls.MOVIE
    elif label == '[ファイル]':
      return cls.FILE
    elif label == '[スタンプ]':
      return cls.STAMP
    elif label == '[連絡先]':
      return cls.CONTACT
    else:
      return cls.NONE
    
