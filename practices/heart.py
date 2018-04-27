import turtle as t
import math as m

t.setup()

t.fillcolor("red")
t.seth(130)
t.begin_fill()
t.circle(100,200)
a=100*m.cos(m.radians(40))+100*m.sin(m.radians(30))
aa=a/m.cos(m.radians(30))
t.fd(aa)
t.up()
t.goto(0,0)
t.down()
t.seth(50)
t.circle(-100,200)
t.fd(aa)
t.end_fill()
t.up()
t.goto(300,300)

t.done()
