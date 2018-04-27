#3.4.py
str = input('请输入一个字符串：')
if str==str[::-1]:
  print("回文")
else:
  print("非回文")