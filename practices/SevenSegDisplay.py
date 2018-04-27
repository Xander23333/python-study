#SevenSegDisplay.py
import time
import turtle as t

def drawLine(draw):
  if (draw == -1):
    t.seth(90)
    return 
  else:
    t.pendown() if draw == True else t.penup()
  t.fd(40)
  t.right(90)
  return 

Judge = [[2,3,4,5,6,8,9],[0,1,3,4,5,6,7,8,9],[0,2,3,5,6,8,9],\
         [0,2,6,8],-1,[0,4,5,6,8,9],[0,2,3,5,6,7,8,9],[0,1,2,3,4,7,8,9]]
def drawNum(num):
#  global Judge
  Lines = []
  for numbers in Judge:
    if numbers == -1:
      aa = -1
    else:
      aa = True if num in numbers else False
    Lines.append(aa)

  print(Lines)
  for i in Lines:
    drawLine(i)
  t.penup()
  t.seth(0)
  t.fd(20)

def drawDate(date):
  t.pencolor("red")
  for i in date:
    if i=='y':
      t.write('年', font = ('Arial', 18, 'normal'))
      t.pencolor('green')
      t.fd(40)
    elif i=='m':
      t.write('月', font = ('Arial', 18, 'normal'))
      t.pencolor('blue')
      t.fd(40)
    elif i=='d':
      t.write('日', font = ('Arial', 18, 'normal'))
    else:
      drawNum(eval(i))

if __name__ == '__main__':
  t.setup(1000,200)
  t.pen(pendown = False,speed = 5, pensize = 5)
  t.goto(-250,0)
  
  str = time.strftime("%Yy%mm%dd",time.gmtime())
  drawDate(str)
  t.done()