#baidu_robots.py
import request_frame

urls = ['www.google.com','www.baidu.com','news.sina.com.cn','www.qq.com','news.qq.com']#'www.moe.edu.cn','www.cugb.edu.cn','www.tsinghua.edu.cn','www.pku.edu.cn']
for url in urls:
  print('\rprocessing {}{}'.format(url,' '*10),end='')
  name = url.split('.')[0]+'_'+url.split('.')[1]
  url = "http://{}/robots.txt".format(url)
  f = open("./robots/{}_robots.txt".format(name),"w")
  print(request_frame.getHTMLText(url),file = f)
print()