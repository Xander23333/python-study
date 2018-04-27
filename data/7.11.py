#7.11.py
with open("test.csv","r") as f:
  ls = []
  for raw in f:
    line = raw.replace("\n","")
    ls.append( line.split(",") )

for i in range(len(ls)):
  for j in range(len(ls[i])):
    try:
      num = eval(ls[i][j])
    except (SyntaxError,NameError):
      continue
    else:
      ls[i][j] = '{:.1f}%'.format(num/100)

with open("testout.csv","w") as f:
  for raw in ls:
    f.write(','.join(raw)+'\n')