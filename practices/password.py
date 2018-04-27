s=input()
for ch in s:
  if ch!=' ':
    print(chr((ord(ch)-ord('a')+3)%26+ord('a')),end='')
  else:
    print(' ',end='')
print()