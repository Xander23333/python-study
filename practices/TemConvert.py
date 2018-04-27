#TemConvert.py
TemStr=input("请输入带符号的温度值：")
if TemStr[-1] in ('C','c'):
    print("转换后的温度为：{:.2f}F".format(eval(TemStr[0:-1]) *1.8 +32))
elif TemStr[-1] in ('F','f'):
  print("转换后的温度为：{:.2f}C".format((eval(TemStr[0:-1])-32)/1.8))
else:
  print("输入格式错误")
  