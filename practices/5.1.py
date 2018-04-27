#5.1.py
def tian(n):
  for i in range(n):
    print(' - - - - '.join( '+'*(n+1) ))
    for j in range(4):
      print( (' '*9).join('|'*(n+1)))
  print(' - - - - '.join( '+'*(n+1) ))
  
n = eval(input('input n:'))
tian(n)