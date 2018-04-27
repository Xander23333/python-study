#4.2.py
str = input("请输入一行字符：")

numcnt=spacecnt=chacnt=other=0

for i in str:
  if i.isspace():
    spacecnt+=1
  elif i.isdigit():
    numcnt+=1
  elif i.isalpha():
    chacnt+=1
  else:
    other+=1

print("英文字符：{}   数字：{}   空格：{}   其他字符：{}".format(chacnt,numcnt,spacecnt,other))