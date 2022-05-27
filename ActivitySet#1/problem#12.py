# Regular Expressions
# https://www.py4e.com/lessons/regex

import re

filename=input("Insert file name:")
fhand=open(filename)
for line in fhand:
  if "From:" in line:
    words=re.findall([0-9]+, 0)