#goat_gate.py
from random import randint
from random import choice
from tqdm import trange

def left(a,b):#函数left：3扇门里除了a和b剩下的门里随机选一扇（a和b可能相等）
  l = []
  for i in range(1,4):
    if i!=a and i!=b:
      l.append(i)
  return choice(l)

if __name__ == '__main__':#主程序
  hits = 0 #换门后猜中的次数
  N = 1000000  # 模拟次数。只有一块cpu所以次数就不设太大了。
  for t in trange(N): 
    car = randint(1,3) #随机一扇门里放汽车
    guess = randint(1,3) #参赛者随机选一扇门
    host = left(car,guess) #主持人从剩下的门（除了参赛者选的和汽车所在的）里选一扇门
    change = left(host,guess) #参赛者看到主持人打开的门后的山羊，选择换成另一扇门
    if change == car: 
      hits += 1 #假如猜中，猜中次数+1

  P = hits/N # 猜中次数/模拟次数 = 换门后猜中的概率
  print("换一扇门中奖的概率是{}，不换中奖的概率是{}".format(P,1-P))