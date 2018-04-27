from PIL import Image

im = Image.open("1.jpg")
r,g,b = im.split()
om = Image.merge("RGB",(b,g,r))
om.save("6.jpg")