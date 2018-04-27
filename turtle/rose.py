from turtle import *

def move(_pos,_h):
  up()
  goto(_pos)
  seth(_h)
  down()

def out():
  print(pos(),heading())  

def lleaf():
  #(45.55,-59.11) 90.0
  move((45.55,-59.11),90.0)

  begin_fill()
  circle(-80,100)
  right(90)
  fd(10)
  left(20)
  circle(-63,127)
  
  up()
  left(50)
  fd(20)
  left(180)
  
  down()
  circle(200,25)
  end_fill()

def rleaf():
  #(61.71,-190.85) 218.0
  move((61.71,-190.85),218.0)

  begin_fill()
  circle(-100,80)
  right(150)
  fd(10)
  left(60)
  circle(-80,98)
  
  up()
  left(60)
  fd(13)
  left(180)
  down()
  
  circle(-200,23)
  end_fill()

def stamen():
  # 1.5 circle
  move((0,250),0)

  circle(50,30) 
  for i in range(10):
      fd(1)
      left(10)
  circle(40,40)

  for i in range(6):
      fd(1)
      left(3)
  circle(80,40)

  for i in range(20):
      fd(0.5)
      left(5)
  circle(80,45)
  left(120)
  fd(20)

  fd(-20)
  right(120)
  
  for i in range(10):
      fd(2)
      left(1)
  circle(80,25)
  
def outline():
  #draw the outline and fill with color
  #(57.77,260.71) 48.0
  move((57.77,260.71),48.0)

  begin_fill()
  for i in range(20):
      fd(1)
      left(4)
  circle(50,50)

  circle(120,55)  
  #+0.5circle
  seth(-90)
  fd(70)
  
  right(150)
  fd(20)
  
  left(140)
  circle(140,90)
  
  left(30)
  circle(160,100)
  # the big circle
  left(130)
  fd(15)
  pos3=pos()

  move((57.77,260.71),40)
  
  circle(-30,70) 
  goto(pos3)
  
  end_fill()

def stick():
  # (97.43,254.48) 305.0
  move((97.43,254.48) ,305.0)

  circle(-20,90) 
  fd(75)
  
  circle(90,110)
  
  up()
  left(162)
  fd(185)
  left(170)
  down()
  circle(200,10)
  circle(100,40)
  circle(-52,115)
  left(20)
  circle(100,20)
  circle(300,20)

  fd(250)

#-----------main-----------
setup(1000,1000,0,0)
speed(0)


fillcolor('red')
outline()
stamen()
stick()

fillcolor('green')
lleaf()
rleaf()

move((200,-200),0)
write("for the Amazing World", True, align="left",font=("Arial",25,"normal"))

exitonclick()