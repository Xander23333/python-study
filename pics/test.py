from PIL import Image

im = Image.open("1.jpg")
r, g, b = im.split()
newg = g.point(lambda i:i*0.9)
newb = b.point(lambda b:b<100)
om = Image.merge("RGB",(r,0,0))
om.save("2.jpg")