#7.1.py
with open("text//7.1.txt","rt") as t:
  print(t.read())

with open("text/7.1.txt","rb") as t:
  print(t.read())

str = b'\xe4\xb8\xad\xe5\x9b\xbd\xe6\x98\xaf\xe4\xb8\xaa\xe4\xbc\x9f\xe5\xa4\xa7\xe7\x9a\x84\xe5\x9b\xbd\xe5\xae\xb6\xef\xbc\x81\n'
print(bytes(str).decode())
print(chr(0xe4),chr(0xb8))