SUM = 0
for I in range(1, 11):
     if I % 2 == 0:
        continue
     if I % 10 == 5:
        break
     SUM = SUM + I
     print(I)
print(SUM)