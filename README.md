# line-log2py
Import Line Talk History to Python (Supported in Japanese only)

## 概要

テキスト分析等の目的でチャットアプリのLINEでのトーク履歴をファイルからインポートするのを助けるライブラリです．LINEのトークルーム設定画面->その他->「トーク履歴を送信」で出力できるテキストファイルの入力に対応しています．現時点では，言語設定が日本語になっているLINEからの出力にしか対応していません．

## インストール

PyPIでインストールできます．

```
# PyPI
pip install line-log2py
```

## 使用方法

`Reader`でファイルを読み込むと`Message`クラスのリストが出力されます．

```
from line-log2py import Reader

file = './line_history.txt'

messages = Reader.readFile(file)

```

## Documentation

### Message

#### Properties

`datetime: datetime`  メッセージが送信された日時
`username: str` ユーザの表示名
`textlines: list[str]`  メッセージの行毎の文章
`kind: Category`  メッセージの種類（テキスト，スタンプ，写真など）

#### Methods

`def addMessage(self, text: str) -> None` 文章に行を追加
`def asList(self) -> list[str]`  内容をリスト形式で出力


### Category

#### Members

- UNDEFINED
- TEXT
- IMAGE
- MOVIE
- STAMP
- FILE
- CALL
- CALL_CANCELLED
- CALL_MISSED
- CONTACT

### Reader

#### Methods

`def readFile(file: str) -> list[Message]` 与えられたパスのファイルを読み込んで`Message`のリストを返す

