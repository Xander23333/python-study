#2.7.py
import turtle as t

t.setup(1000,1000)
t.pen(shown = True, pendown = False, speed = 10)

a = 100*pow(3,0.5)

t.goto(-100,0)
t.seth(30)
t.pendown()
for i in range(3):
  t.fd(a)
  t.right(120)
t.penup()
t.goto(100,0)
t.seth(-150)
t.pendown()
for i in range(3):
  t.fd(a)
  t.right(120)

t.done()