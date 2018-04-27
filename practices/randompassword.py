#randompassword.py
from random import choice
s=''
for i in (65,97):
  for j in range(26):
    s+=chr(i+j)
for i in range(10):
  s+=chr(48+i)

for t in range(10):
  pw = ''
  for i in range(8):
    pw+=choice(s)
  print(pw)