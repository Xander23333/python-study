from time import perf_counter 
from random import random

def MonteCarlo(n):
  start=perf_counter()

  DARTS=n*n
  fits=0
  for i in range(DARTS+1):
    print('\rprocessing {}'.format(i),end = '')
    x,y=random(),random()
    d=x**2+y**2
    if d<=1.0:
      fits+=1
  print()
  print("Time cost is {}".format(perf_counter()-start))
  return fits/DARTS*4

def Formula(n):
  start=perf_counter()

  pi=0
  for k in range(n):
    pi+=(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))/pow(16,k)
  
  print("Time cost is {}".format(perf_counter()-start))
  return pi

print("{} by Monte Carlo Method is {}".format(chr(0x03C0),MonteCarlo(1000)))
print("{} by Formula is {}".format(chr(0x03C0),Formula(200)))
