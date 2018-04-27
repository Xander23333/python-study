#upperpy.py
# name = input("name of program:")
name = 'test.py'
with open(name,"r") as f:
  text = f.read()
print("# program origin:\n")
print(text)


from keyword import kwlist
with open("build-in_func.txt","r") as fr:
  text1 = fr.read()
  ls = text1.split()
  for i in range(len(ls)):
    ls[i] = ls[i].strip(')')
kwlist += ls
kwlist.sort(key = lambda x:len(x) , reverse = True)
# print(kwlist)

text = text.upper()
for kw in kwlist:
  text = text.replace(kw.upper(),kw)
print("\n# program upper:\n")
print(text)

name2 = "uppertest.py"
with open(name2,"w") as fw:
  fw.write(text)

print("\n# output:")
import os
ls = os.popen('python {}'.format(name2)).readlines()
for i in ls:
  print(i)
