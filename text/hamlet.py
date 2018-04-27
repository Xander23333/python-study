#hamlet.py

with open("text/hamlet.txt","r") as f:
#去噪
  punc = "`~!@#$%^&*()-_=+[{]}|\\:;\"\'<,>.?/"
  noise = ['and','this','that','the','and','to','of','i','you','a','my','in','it','is','are','am','there','here','with','not','his','but','for','with','your','s','me','he','be','as','what','how','him','s','o','do','will','no','all','by']

  tex = f.read()
  tex = tex.lower()
  for ch in punc:
    tex = tex.replace(ch,' ')
    
  for ch in noise:
    tex = tex.replace(' '+ch+' ',' ')
  
#统计词频
  words = tex.split()
  counts = {}
  for word in words:
    counts[word] = counts.get(word,0)+1

#排序输出
  items = list(counts.items())  # a list of tuple
  items.sort(key = lambda x:x[1], reverse = True)
  for i in range(10):
    word, count = items[i]
    print("{:<10}{:>5}".format(word,count))

