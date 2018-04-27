#task1.py
import request_frame
import time

url = "http://www.baidu.com"
start = time.perf_counter()
N=100
for i in range(N):
  request_frame.getHTMLText(url)
  print("\rprocessing {}".format(i),end='')
print()
print("爬取百度页面{}次的时间是{:.4f}s".format(N,time.perf_counter()-start ))
