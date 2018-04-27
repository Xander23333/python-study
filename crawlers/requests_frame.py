#frame.py
import requests
import os

def getHTMLText(url,kv={}):
  try:
    r = requests.get(url, timeout=10,params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    print("产生异常")
    return "" 

def getHTMLPic(url, root):
  try:
    path = root + url.split('/')[-1]
    if not os.path.exists(root):
      os.mkdir(root)
    if not os.path.exists(path):
      r = requests.get(url, timeout = 10)
      with open(path,'wb') as f:
        f.write(r.content)
        print('文件保存成功')
    else:
      print('文件已经存在')
  except:
    print('爬取失败')

if __name__ == "__main__":
  
  
  url = 'https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=f7101b81fdfaaf5180e386bdbc5594ed/7e3e6709c93d70cf02cc19aaf8dcd100baa12b66.jpg'
  root = './/pictures//'
  getHTMLPic(url,root)