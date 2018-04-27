#CalBMI.py
height,weight = eval(input("身高（米）和体重（公斤），请用逗号隔开："))
bmi=weight/pow(height,2)
print("BMI 数值为:{:.5f}".format(bmi))
dom=""
nat=""
if bmi<18.5:
  dom=nat="偏瘦"
elif bmi<24:
  dom=nat="正常"
elif bmi<25:
  dom,nat="偏胖","正常"
elif bmi<28:
  dom,nat="偏胖","偏胖"
elif bmi<30:
  dom,nat="肥胖","偏胖"  
else:
  dom=nat="肥胖"

print("BMI 指标为:国际'{}' 国内'{}'".format(nat,dom))
