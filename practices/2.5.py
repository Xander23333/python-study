#TemConvert.py
TemStr=input()
if TemStr[-1] == 'm':
    print("{:.3f}in".format(eval(TemStr[0:-1]) *39.37))
elif TemStr[-1] =='n':
  print("{:.3f}m".format(eval(TemStr[0:-2])/39.37))
else:
  print("输入格式错误")
  