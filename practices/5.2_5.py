#5.2_5.py
def isOdd(x):
  return True if x&1 else False

def isNum(s):
  try:
    eval(s)
  except:
    print('NO!')
    return False
  else:
    print('Yes',eval(s))
    return True

def multi(*b):
  ans = 1 
  for i in b:
    ans = ans*i
  return ans

def isPrime(x):
  try:
    x = int(x)
  except ValueError:
    print("请输入整数！")
  else:
    for i in range(2,int(pow(x,0.5))+1):
      if x%i==0 :
        return False
    return True

while(True):
  x=input()
  print(isPrime(x))