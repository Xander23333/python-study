#2.6.py
import turtle as t

t.setup(1000,1000)
t.pen(shown = True, pendown = False, speed = 0)
t.goto(-200,-200)

for i in range(4):
  t.penup()
  t.fd(100)
  t.pendown()
  t.fd(200)
  t.penup()
  t.fd(100)
  t.left(90)

t.hideturtle()
t.done()
