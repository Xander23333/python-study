#search.py
import request_frame

if __name__=='__main__':
  url1 = 'http://www.baidu.com/s'
  kv1 = {'wd':'徐翔'}
  r1 = request_frame.getHTMLText(url1,kv1)
  print(r1.count('徐翔'),len(r1))

  url2 = 'http://www.so.com/s'
  kv2 = {'q':'Python'}
  r2 = request_frame.getHTMLText(url2,kv2)
  print(r2.count('Python'),len(r2))