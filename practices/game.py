#game.py
from random import randint

cnt=0
num = randint(0,100)
while(True):
  try:
    guess =  eval(input("请猜一个0到100间的数字："))
  except:
    print("输入内容必须为整数！")
    continue
  else:
    cnt+=1
    if guess == num:
      print("预测{}次，你猜中了！".format(cnt))
      break
    elif guess > num:
      print("遗憾，太大了")
    else:
      print("遗憾，太小了")
