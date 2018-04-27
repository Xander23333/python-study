#RedMensions.py
import jieba

def getText():
  with open("source/红楼梦.txt","r",encoding='gb18030') as f:
    tex = f.read()
    return tex  
    # print(tex.encode('iso-8859-1').decode('utf-8'))


tex = getText()
words = jieba.lcut(tex)
counts = {}

for word in words:
  if len(word)==1:
    continue
  elif word == "宝玉" or word == "二爷":
      rword = "宝玉"
  elif word == "王夫人" or word == "王熙凤" or word == "凤姐儿" or word == '凤姐':
      rword = "凤姐"
  elif word == "老太太" or word == "贾母":
      rword = "贾母"
  else:
      rword = word
  counts[rword] = counts.get(rword,0) + 1
  
exclude = ['什么', '我们', '那里', '你们', '如今', '说道', '知道', '起来', '姑娘', '这里', '出来', '他们', '众人', '自己', '一面', '太太', '只见', '怎么', '奶奶', '两个', '没有', '不是', '不知', '这个', '听见', '这样', '进来', '咱们', '告诉', '就是', '东西', '回来', '只是', '大家', '老爷', '只得', '丫头', '这些', '不敢', '出去', '所以', '不过', '的话', '不好', '姐姐', '一时', '不能', '过来', '心里', '如此', '今日', '银子', '几个', '答应', '二人', '还有', '只管', '这么', '说话', '一回', '那边', '湘云', '这话', '外头', '打发', '自然', '今儿', '罢了', '屋里', '那些', '听说', '小丫头', '一个', '问道', '看见', '妹妹', '人家', '不用', '媳妇', '如何', '原来', '一声', '一句', '家里', '不得', '到底', '这会子', '进去', '姊妹', '别人', '回去', '明儿', '丫鬟', '过去', '连忙', '心中', '方才', '还是', '婆子']
for ch in exclude:
  del counts[ch]

if __name__=='__main__':
  items = list(counts.items())
  items.sort(key = lambda x:x[1], reverse = True)
  """  
  # 人工去噪：去除非人名，保留前15人名
  cnt = 18
  i = 18
  while(cnt<20):
    word,count = items[i]
    i += 1
    ch = input("{:<10}{:>5}  (y/n)".format(word, count))
    if ch=='n':
      exclude.append(word)
      del counts[word]
    else:
      cnt+=1  
  print(exclude)
  """
  # 输出结果
  items = list(counts.items())
  items.sort(key = lambda x:x[1], reverse = True)
  for i in range(20):
    word,count = items[i]
    print("{:<5}{:\u3000<8}{:>8}".format(i+1, word, count))

