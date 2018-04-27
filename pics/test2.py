from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

im = Image.open('1.jpg')

r, g, b = im.split()
newg = g.point(lambda i:i*0.9)
newb = b.point(lambda b:b<100)
om1 = Image.merge("RGB",(r,newg,newb))
om1.save("11.jpg")
newr = r.point(lambda i:0)
om12 = Image.merge("RGB",(newr,g,b))
om12.save("12.jpg")

om2 = im.filter(ImageFilter.CONTOUR)
om2.save('3.jpg')

om3 = ImageEnhance.Contrast(im)
print(type(om3))
om3.enhance(20).save('4.jpg')

