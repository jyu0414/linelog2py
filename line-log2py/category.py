from enum import Enum

class Category(Enum):
  UNDEFINED = Enum.UNDEFINED
  TEXT = 1
  IMAGE = 2
  MOVIE = 3
  STAMP = 4
  FILE = 5
  CALL = 6
  CALL_CANCELLED = 7
  CALL_MISSED = 8
  CONTACT = 9

  def __init__(self, label: str):
    if label == '[写真]':
      self = self.IMAGE
    elif label == '[動画]':
      self = self.MOVIE
    elif label == '[ファイル]':
      self = self.FILE
    elif label == '[スタンプ]':
      self = self.STAMP
    elif label == '[連絡先]':
      self = self.CONTACT
    else:
      self = self.UNDEFINED
