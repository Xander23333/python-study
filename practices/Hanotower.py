#Hanotower.py

cnt = 0
def move(start,dest,num):
  global cnt
  if num==1:
    print("{}->{}".format(start,dest))
    cnt+=1
    return 1
  mid = 6-start-dest
  move(start,mid,num-1)
  cnt+=1 
  print("{}->{}".format(start,dest))
  move(mid,dest,num-1)

move(1,3,3)
print(cnt)