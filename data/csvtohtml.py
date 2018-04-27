# csvtohtml.py
seg1 = '''<!DOCTYPE HTML>\n<html>\n<body>\n<meta charset=gb2312>
<h2 align=center>2016年7月部分大中城市新建住宅价格指数</h2>
<table border='1' align="center" width=70%>
<tr bgcolor='skyblue'>\n'''
seg2 = "</tr>\n"
seg3 = "</table>\n</body>\n</html>"


def fill_data(locls):
    seg = ''
    for i in locls:
      seg += '<td align="center">{}</td>'.format(i)
    seg = '<tr>{}</tr>\n'.format(seg)
    return seg

with open("test.csv", "r") as fr:
  ls = []
  for line in fr:
      line = line.replace("\n", "")
      ls.append(line.split(","))
# title
with open("price2016.html", "w", encoding = 'gb18030') as fw:
  fw.write(seg1)
  
  seg = ''
  for i in ls[0]:
    seg += '<th width="25%">{}</th>\n'.format(i)
  fw.write(seg)

  fw.write(seg2)
  
  for line in ls[1:]:
    fw.write(fill_data(line))
  
  fw.write(seg3)
  