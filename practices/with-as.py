#with-as.py

class test:
  def __enter__(self):
    print("enter!")

  def __exit__(self,value, trace):
    print("exit!")

if __name__ == "__main__":
  with test() as t:
    print('yes')