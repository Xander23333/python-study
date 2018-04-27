import turtle as t
import time
t.setup()
t.color("black","red")

t.speed(10)
t.penup()
t.goto(0,100)
t.pendown()
t.seth(-108)
t.begin_fill()
for i in range(5):
  t.fd(200)
  t.left(144)
t.up()
t.end_fill()
time.sleep(2)

t.done()

# 卧槽没发涂满是什么鬼