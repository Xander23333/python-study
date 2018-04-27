#text.py
import requests
import os


def getHTMLText(url, root):
  try:
    path = root + url.split('/')[-1]
    if not os.path.exists(root):
      os.mkdir(root)
    if not os.path.exists(path):
      r = requests.get(url, timeout = 10)
      r.encoding = r.apparent_encoding
      with open(path,'w') as f:
        f.write(r.text)
        print('文件保存成功')
  except:
    print('爬取失败')

url1 = 'http://python123.io/resources/pye/hamlet.txt'
url2 = 'http://python123.io/resources/pye/threekingdoms.txt'
getHTMLText(url2, root = '..//text//')
