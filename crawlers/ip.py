#ip.py
import requests_frame
import re

if __name__ == '__main__':
  url = 'https://ip.cn/index.php?ip='
  ip = '123.123.123.123'
  text = requests_frame.getHTMLText(url+ip)
  #print(text)  
  t1 = re.search('(?<=GeoIP: )(.*?)(?=</p></div>)',text).group(0)
  print(t1)
  print('您搜索的ip地址是：'+ip)
  print('此ip的位置为：')
  print(re.search('(.*)(?=</p>)',t1).group(0))
  print('服务商为：')
  print(re.search('(?<=<p>)(.*)',t1).group(0))
  