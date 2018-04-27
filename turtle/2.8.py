#2.8.py
import turtle as t

#2.7.py
import turtle as t

t.setup(1000,1000)
t.pen(shown = True, pendown = False, speed = 0)

a = 500
t.goto(-250,-250)
t.seth(90)
t.pendown()
while(a!=0):
  t.fd(a)
  a-=2.5
  t.right(90)

t.ht()
t.done()