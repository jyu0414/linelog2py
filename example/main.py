from linelog2py import *

messages = Reader.readFile("example.txt")

for message in messages:
  print(message)