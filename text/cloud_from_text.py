#cloud.py
from wordcloud import WordCloud, ImageColorGenerator, random_color_func, STOPWORDS
import matplotlib.pyplot as plt
from os import path

d = path.dirname(__file__)

#mask
mask = plt.imread(path.join(d,"source/dufu.jpg"))
print("图片打开成功")
#word
STOPWORDS.add("杜甫")
wc = WordCloud(font_path = "/System/Library/Fonts/STHeiti Medium.ttc" , 
                mask = mask, width = 1000, 
                height = 1000, background_color = "black", 
                max_font_size=62, min_font_size=5,
                stopwords = STOPWORDS)
print("WordCloud创建成功")
                
#generate
import jieba
with open("source/《杜甫诗》全集.txt",encoding = 'gb18030') as f:
  text = f.read()
  text = " ".join(jieba.lcut(text))
  dict = wc.process_text(text)
  # print(dict)
  wc.generate_from_frequencies(dict)
  # wc.generate(text)
print("词云生成成功")

#color
color_func = ImageColorGenerator(mask)
wc.recolor(color_func = color_func)
print("染色成功")

#show
plt.imshow(wc)
plt.axis('off')
plt.show()
#save
wc.to_file("cloud_dufu.jpg")
print("保存成功")
