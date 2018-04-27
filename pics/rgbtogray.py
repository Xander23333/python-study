#rgbtogray.py
from PIL import Image

if __name__ == '__main__':
  im = Image.open("fruit.png")
  om = Image.new(mode = 'L', size = im.size, color=0)
  om2 = Image.new(mode = 'RGB', size = im.size, color=0)
  
  width, height = im.size
  for i in range(width):
    for j in range(height):
      r,g,b,a = im.getpixel((i,j))
      gray = int(0.2126*r+0.7152*g+0.0722*b)
      om.putpixel((i,j), (gray,) )
      om2.putpixel((i,j),(r,0,0) )  

  om.save("fruit_gray.jpg")
  im.convert("L").save("fruit_gray2.jpg")
  om2.save("fruit_rr.jpg")
  # 用了最蠢的方法，逐个像素点赋值