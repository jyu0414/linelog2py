import sys
sys.path.append("../linelog2py")
from linelog2py import *

messages = Reader.readFile("example/example.txt")

for message in messages:
  print(message)