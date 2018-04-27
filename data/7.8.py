with open("test.csv","r") as f:
  ls = []
  for line in f:
    line = line.replace("\n","")
    ls.append(line.split(","))

print(ls)
