#jd_produce.py
import request_frame

if __name__=="__main__":
  url = 'http://item.jd.com/12198327.html'
  r = request_frame.getHTMLText(url)
  print(r[:1000])