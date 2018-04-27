with open("test.csv","r") as f:
  for line in f:
    line = line.replace("\n","")
    ls = line.split(',')
    print("\t".join(ls)) 
