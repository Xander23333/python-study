#pil_test
from PIL import Image

im2 = Image.open("crawlers/pictures/3.jpg")
print(im2.format, im2.size, im2.mode, im2.palette)

im = Image.open("../crawlers/pictures/4.jpg")
try:
  im.save('picframe{:02d}.png'.format(im.tell()))
  while True:
    im.seek(im.tell()+1)
    im.save('picframe{:02d}.png'.format(im.tell()))
except:
  print('处理结束')