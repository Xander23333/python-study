#test2.py
with open("test2.csv","r") as f:
  for line in f:
    ls = line.split(',')
    for i in ls:
      