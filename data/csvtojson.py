#csvtojson.py

with open("test.csv","r") as fr:
  ls = []
  for line in fr:
    line = line.replace('\n','')
    ls.append(line.split(','))

outls = []
for i in range(1,len(ls)):
  raw = {}
  for j in range(len(ls[i])):
    raw[ls[0][j]] = ls[i][j]
  outls.append(raw)
# print(outls)
import json
with open("price2016.json","w") as fw:
  json.dump(outls,fw,indent=2,sort_keys=True,ensure_ascii=False) #indent缩进