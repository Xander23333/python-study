#6.3.py
def dup(ls):
  se = set(ls)
  if len(se) == len(ls):
    return False
  else:
    return True

def main():
  ls = input().split()
  print(dup(ls))
main()