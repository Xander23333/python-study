#6.5.py
from random import randint
from tqdm import trange

p = 1
for i in range(343,366):
  p = p*i
p = p/pow(365,23)
print("理论上的概率为{}".format(1-p))

N = 100000
hits = 0
for i in trange(N):
  ls = []
  for j in range(23):
    ls.append(randint(1,365))
  if len(set(ls)) != len(ls):
    hits += 1
P = hits/N

print("样本数{}下，23个人至少两人生日相同的概率是{:.10f}".format(N,P))