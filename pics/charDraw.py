#charDraw.py
from PIL import Image
from tqdm import tqdm
from random import choice

ascii_char1 = '@#$%&*qwertyuiopasdfghvbnm2346890  '
ascii_char = '01010101010101 '
lenc = len(ascii_char)
#print("lenc = {}".format(lenc))

def get_char(r,g,b,alpha = 256):
  gray = int(0.2126*r + 0.7152*g + 0.0722*b)
  if gray > 240:
    ch = ' '
  else:
    ch = choice('01')
  #print("gray={} unit={} index={}".format(gray,unit,index))
  return ch

if __name__=='__main__':
  targets = ['py','zhihu','taobao','jd','baidu']
  size = 50

  for target in targets:
    im = Image.open("icon//{}.jpeg".format(target))
    width, height = im.size
    width = 2*int(size*width/max(width,height))
    height = int(size*height/max(width,height)) 
    im = im.resize((width,height))
  #  im.save("why.jpeg")
    s = ''
    with tqdm(total = height*width) as qbar:
      for i in range(height):
        for j in range(width):
          qbar.update(1)
          s += get_char(*im.getpixel((j,i)))
        s += '\n'

    with open("icon//{}.txt".format(target),"w") as f:
      f.write(s)


