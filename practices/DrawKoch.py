#DrawKoch.py
import turtle as t

def koch(size, n):
  if n==0:
    t.fd(size)
  else:
    for angle in [0,60,-120,60]:
      t.left(angle)
      koch(size/3,n-1)

if __name__=='__main__':
  t.setup(1000,1000)
  t.pen(speed = 0, pendown = False, pencolor = 'blue')
 
  a,n = 400,4
  t.goto(-a/2,a/2/pow(3,0.5))
  t.pd()
  for i in range(3):
    koch(a,n)
    t.right(120)
  t.ht()
  t.done()