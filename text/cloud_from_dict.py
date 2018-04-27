#cloud.py
from wordcloud import WordCloud, ImageColorGenerator, random_color_func, STOPWORDS,get_single_color_func
import matplotlib.pyplot as plt

name = 'tk'
image_url = 'source/lvbu.jpg'
background_color = 'black'
font_path = "/System/Library/Fonts/STHeiti Medium.ttc"

from PIL import Image
#mask
mask = plt.imread(image_url)
im = Image.open(image_url)
print("图片打开成功")
#word
wc = WordCloud(font_path = font_path , 
                mask = mask, width = 1000, 
                height = 1000, background_color = background_color, 
                stopwords = STOPWORDS , max_font_size=int(im.size[1]/10),min_font_size=15
                )
print("WordCloud创建成功")
                
#generate from dict
from threeKingdoms import counts
wc.generate_from_frequencies(counts)
print("词云生成成功")

#color
color_func = ImageColorGenerator(mask)
color_func2 = get_single_color_func('white')
wc.recolor(color_func = color_func2)
print("染色成功")

#show
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
#save
wc.to_file("cloud_{}.jpg".format(name))
print("保存成功")
