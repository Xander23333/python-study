- 编译和解释，脚本语言与静态语言
- 算法是程序的灵魂
- IPO
- 计算思维=抽象+自动化

print(*objects, sep=' ', end='\n', file=sys.stdout)    
a = b if <express> else c   
hash(<list>)    
sorted(<list>[,key[,reverse])       
list.sort(...)

print({:02d}.format(20))
 

---

## 目录： 
0. 计算思维
1. 数值数据类型
2. 字符串
3. 分支结构
4. 组合数据类型
5. 文件
6. \* 各种库的常用函数

 

---

 
### 0 计算思维
用计算机解决问题的步骤：
1. 分析问题：抽象以确定可计算部分
2. 确定边界：定义input和output
3. 设计算法：分治地设计process
4. 程序实现：根据需要选择语言
5. 调试测试：单元测试和集成测试
6. 升级维护

>Talk is cheap. Show me the code.   --Linus Torvalds

### 1 数值数据类型
##### 1.1 类型
-  整数  
无范围限制（要在内存限制内）。  
四种进制（大小写都可）：  (),0b,0o,0x

-  浮点数    
    - 范围：精度1e-16, 范围 -1e308 ~ 1e308
    - **出现不确定尾数**：

        二进制和十进制的小数不是一一对应的(?)，因此计算机计算浮点数时（如0.1对应的二进制小数是无穷循环），转换成二进制再运算再转化回十进制，中间就会出现误差（例如0.1+0.2=0.30000000000000004），这是浮点数储存机制导致的无法避免的问题。因此浮点数一定要注意精度范围，比较时要用round函数。

- 复数

##### 1.2 二元数值运算符
+, -, * , / ,   
// , \*\* , % 

##### 1.3 数值运算函数
- 计算      
abs     
divmod(x,y) = (x//y,x%y)    
pow(x,y[,z]) = (x**y)%z     
round(a[,b])    
max,min
- 数据类型转换        
int,float,complex  可直接转换字符串

### 2 字符串
##### 2.1 表示方法
四种:' '," ",""" """,''' '''
后两种相当于注释

冗余的好处是使'和"的出现变得简便

##### 2.2 索引和切片
索引：<str>[M]

切片：<str>[M:N:K]
e.p. <str>[::-1]

##### 2.3 操作符
\+ \* in

##### 2.4 函数
len(汉字、字母、数字都是1个字符) , str-eval, hex-oct-bin , chr-ord

##### 2.5 Unicode编码
ASCLL码只包括了英文字母和常用字符，因此全世界共同制定了一个编码使得人类的所有字符都包含在内，以便计算机使用。这个编码就是Unicode编码，它的范围为(0x000000-0x10FFFF)，每个编码对应一个字符。

##### 2.6 方法
方法特指\<a\>.\<b\>()风格中的函数\<b\>()（oo的一个概念）

- 状态  
count(sub[, start[, end]])(non-overlapping)  
isdigit,  istitle, isupper, islower, isspace, isalpha, is alnum   
(only unicode)  isnumeric, isdecimal 

isdigit是判断是否全由数字构成

- 处理  
lower()-upper()         
split(sep=None, maxsplit=-1)    
replace(old, new[, count])  
center(width[,fillchar])        
strip([chars])      
join(iterable)  

##### 2.7 格式化
- format    
<模板字符串>.format(<参数>)     
槽{<参数序号>:<格式控制标记>}   
格式控制标记：  
<填充(char)><对齐(</^/>)><宽度(int)><,><.精度(f/str)><类型(b/o/d/x/X/c/e/E/f/%)>

### 3 分支结构
for in - else   
while - else    
if elif else    
try except else finally

### 4 组合数据类型
##### 4.1 序列:list,str,tuple
切片，join
sorted
max-min
len index count
hash
- list  append,reverse

##### 4.2 集合:set
集合运算
pop,add

##### 4.3 映射:dict
keys values items get pop del

### 5 文件

##### 5.1 打开
函数|作用
----|---
open("fileaddress",mode,encoding) |return a file type  
mode = r , w/x/a , +, t/b   |
close()|
##### 5.2 读    
函数|作用
----|---
read(hint=-1)| return a str or bytes(manylines)     
readline(hint=-1)| return a str or bytes(one line)  
readlines(hint=-1) | return a list of strs or byteses (many lines)

##### 5.3 写
函数|作用
----|---
write(s)| s is a str or bytes           
writelines(hint=-1)| s is a list of strs or byteses         
seek(offset)| move the seek, 0 - begin, 1 - right here, 2 - end

#### 字符集和编码
计算机中的所有文件都是二进制数字。  
我们日常生活中的信息，文本、视频、软件，要存储在计算机中，都要变成二进制数字。  
如何让信息与二进制数字对应？于是我们发明了编码。计算机中所谓编码，就是信息与二进制数字的映射。    

文本的编码，一开始只有ASCII码。     
这个编码只包含了英文字母和一些常用字符，当计算机传播到其他非英语国家时已经不够使用了，因此每个国家往往有自己的民族语言对应的编码，比如中国的GB18030、GBK等等，国家自己的编码一般向下兼容ASCII。     
后来，随着互联网的发明，不同国家间的信息交流愈加密切，但是各个国家自己的编码并不互相兼容，这导致了信息交流的障碍。因此，计算机业界于1990年开始研制一种包含人类所有语言文字和通用符号的编码，并于1994年发布。这种编码就叫Unicode。

无论一个文件采取何种编码，它在计算机中都是二进制数字。当我们想要查看这个文件，也就是需要将它从二进制数字转换成信息，计算机就对照着该文件的编码将它“翻译”成信息。假如这时候计算机选择了错误的编码，那么该文件就会被“翻译”成错误的信息，也就是我们常见的“乱码”现象。
##### 扩展
1. 我们常见的utf-8编码是什么呢？因为Unicode每个字符对应的都是两字节，直接按照Unicode编码占用的空间非常大，所以人们发明了基于Unicode的更节省空间的编码方式。常见的utf-8就是这种编码之一，它将Unicode编码集分成三部分，分别用一、二、三字节的编码表示，大大节省了空间。
2. utf-8、utf-16、utf-32的区别：同样是变长度编码，不同的是单位长度分别是8、16、32个二进制位，最常用的是utf-8，因为最节省空间。
3. python3的字符串类型，采取的编码是Unicode。如果一个文本不是用Unicode编码，那么python直接读取该文件得到的字符串，就会出现乱码或者读取错误。  



### *1 [time库](https://docs.python.org/3/library/time.html?module-time)
##### 程序计时
函数|作用
----|---
perf_counter()|
process_time()|
sleep(x)  |
##### 时间格式化
函数|作用
----|---
time() |返回1970.1.1 00:00 至今的计时，是浮点数  
ctime() |返回当前系统时间的易读取形式    
gmtime()， calendar.timegm()  |
localtime()， mktime()|

##### 时间获取
tpl为格式控制字符串:
```python
>>> strftime("%Y-%m-%d %b(%B) %a(%A) %H:%M:%S(%I:%M:%S %p)",a)
'2018-04-17 Apr(April) Tue(Tuesday) 16:17:02(04:17:02 PM)'
```
函数|作用
----|---
strftime(tpl,time.struct_time) |格式化输出时间    
strptime(str,tpl) |格式化读取时间
##### 时间数据类型
time.struct_time(tm_year=2018, tm_mon=4, tm_mday=17, tm_hour=4, tm_min=19, tm_sec=9, tm_wday=1, tm_yday=107, tm_isdst=0)

### *2 random库
计算机中的随机数是由种子经过梅森旋转产生的随机数序列中选取的，是伪随机数，因为只要种子固定随机数序列是可以复现的。
函数|作用
----|---
seed(a=None,version=2) |默认是系统时间（微秒）   
random()| a random float in [0.0,1.0)
randint(a,b)| a random int in [a,b] , equal to randrange(a,b+1) 
randrange(a,b[,step])| Return a randomly selected element from range(start, stop, step).  
getrandbits(k)| Returns a Python integer with k random bits.        
uniform(a,b)| a float in [a,b]
choice(seq)| return a random element from the seq    
shuffle(&seq)| shuffle the seq   

### *3 turtle库（待完善）
初始化状态|作用
----|---
“shown”| True/False
“pendown”| True/False
“pencolor”| color-string or color-tuple
“fillcolor”|color-string or color-tuple
“pensize”| positive number
“speed”| number in range 0..10

常用函数|作用
----|---
pendown()=pd()=down()|
penup()=pu=up()|
fd, bw|
left, right|
seth, goto |



### *4 math
Constant : pi e inf nan     
method : fsum(<list>) gcd(a,b) factorial(x)      

### *5 实例：计算圆周率
1. 公式法
```math
\pi=\sum^{\infty}_{k=0} 
\left[
\frac{1}{16^k} \left(
\frac{4}{8k+1} - \frac{2}{8k+4} -\frac{1}{8k+5} -\frac{1}{8k+6}
\right)
\right]
```

2. 蒙特卡罗方法

现在的结果是
```python
Time cost is 0.4726069489843212
π by Monte Carlo Method is 3.140296
Time cost is 0.0007218730170279741
π by Formula is 3.141592653589793
```
蒙特卡罗方法的准确度和耗时都远逊色于公式法，
因为蒙特卡罗方法提高精度需要的计算量非常大。

但是这是两种不同的思维方式。后者用超大的计算量得到结果，前者用分析得出的准确公式，是计算思维（统计）和分析思维的区别。


### *6 tqdm库
精简的进度条库。包含一个类 tqdm，主要方法 initial(iterable , total, desc )，update(int), close()     

##### 自动
tqdm(<iterable>)
或者直接
trange(int)

##### 手动
最好用with-as
```python
pbar = tqdm(total=100, desc='name')
for i in range(10):
    pbar.update(10)
pabr.close()
```

### *7 jieba中文分词库
```python
import jieba

seg_list = jieba.lcut("我来到北京清华大学", cut_all=True) # 全模式

seg_list = jieba.lcut("我来到北京清华大学", cut_all=False) # 精确模式

seg_list = jieba.lcut("他来到了网易杭研大厦")  # 默认是精确模式

seg_list = jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
```
更改字典：add_word, del_word    
调整词频：suggest_freq(segment,tune=True)

### *8 pillow库
##### Image对象
方法|作用
---|---
open(filename)|
new(mode,size,color)|
多帧（图像序列）    |
seek(frame)|跳转到第frame帧   
tell()| 当前序列号
convert(mode)  | 
thumbnail(size) |缩略图（并不知道和resize有何区别）    
resize(size)    |
rotate(angle)   |
point(func) |对每个像素点的每个色道进行func函数    
split() |多色道返回各个色道的单色道副本（RGB返回三个L）
对单独的像素点操作  |
getpixel(xy)        |
putpixel(xy,value)   |   
merge(mode,bands)|单色道合成多色道     
blend(im1,im2,alpha)|return im1*(1-alpha)+im2*alpha 
##### 其他对象
ImageFilter：过滤       
ImageEnhance：增强        


##### 属性      
format，mode，size，palette


### 图像
计算机是如何将储存的图像展示在我们眼前的？  

要讨论这个问题，我们得先从显示屏说起。现代的一切电子显示屏都是由电子元件排列成的。具体来说，当它向我们展示一个画面的时候，这个画面是由无数电子元件的亮灭来展示的。我们称一个单位元件为屏幕的一个像素点。电子屏幕向我们展示的一切画面都以像素点排列的形式表现的。

知道了屏幕是如何展示图像的，我们再来看一下图像是如何储存在计算机中的。

#### 位图
在计算机内部，一切都是数字。一个图像要储存在计算机中，也需要变成数字。我们最常用的将图像数字化的方式，是将图像分割成众多很小的色块的排列。这种方式得到的图像，我们称之为位图。这些色块称作图像的像素点（区别于屏幕的像素点），每个色块的数字信息称为像素值。例如“RGB”色彩模式，那么一个像素点就包含(r,g,b)三个值。色彩模式可以理解为规定一个像素所包含信息的标准，常用的如“L”（灰度，即黑白），“RGB”（三色，最常用的彩色标准）。

位图在计算机内部的储存形式就是像素值的矩阵。例如一个“RGB”模式的2560 x 1600的图片，它在计算机内部实际上是2560X1600个三元组(r,g,b)组成的矩阵。这个矩阵储存了该图片向我们展示的全部信息（不包括附加的信息）。

当位图1：1展示在屏幕上的时候，每个色块就对应着屏幕的一个像素点。当我们将图片放大的时候，实际上是计算机在对图像进行处理，算法是使图像的每个像素点的信息覆盖屏幕的多个像素点。而这种操作对于人类的视觉来说，就是图片随着放大变得模糊了。其实从信息论的角度来说，感觉模糊是因为单位面积内的信息减少了。

#### 矢量图
另一种将图像数字化的方式，是用几何元素分解它，然后储存下几何元素的信息。这种方式并不能很好地表示所有图像，因为现实世界的几何元素非常复杂，因此我们日常的图片往往是位图。使用矢量图表示的一般是计算机绘制的图像，即有清晰的几何结构，如科学计算软件绘制的函数图像，或html被浏览器渲染出来的图像。    
我们可以这样区别矢量图和位图：位图储存的是关于图像的离散信息，矢量图储存的是关于图像的连续信息。

矢量图在计算机内部的储存形式是表示图像结构的代码。如矢量图常见的svg格式，如果你用文本编辑器打开一张svg图片，你会看到它内部是类似网页的html代码。这些代码储存了这种图片的所有结构信息，从而查看图片的软件可以通过这些代码绘制出整张图片。

无论矢量图以任何比例展示在屏幕上，都是查看图片的软件根据代码中的结构信息绘制出当前比例的图像。因此无论放大多少，都不会失真，图像中的结构信息依然没有损失。

#### 总结
计算机中的图片有两种：位图和矢量图。位图是像素矩阵表达的离散的图像。矢量图是根据结构信息实时绘制的连续的图像。

#### 附录
1. svg，xml，html   
svg其实是一种XML格式的语言，和HTML有一些区别，XML格式语言更加严格且扩展性强。暂时说不清楚更多的区别。

2. RGB，RGBA，L，CMYK       
以上是常见的色彩模式。位图的所谓色彩模式，就是规定一个像素点包含的信息有哪些，以及这些信息的含义是什么。L是灰度图，RGB是三通道彩色图，RGBA比RGB增加了一个A透明度通道，CMYK是印刷彩色模式。    
RGB模式下一个像素点包含了(r,g,b)三个颜色通道的数值，将他们结合就得到了这个像素点的颜色。        
当我们用python的pillow库的Image.split方法分解一张RGB图片时，得到是三个单色道的L图片副本，原本RGB对应的三元组信息在分解成单个数值之后意义就变成了灰度值。    
如何将RGB图片转化成灰度图呢？有很多种标准（转化方程），具体请见维基百科的grayscale词条。如何将一张图片转化为字符画呢（比如杂志封面那样非常酷的01数字组成的人脸）？其实很简单，首先将图片转化为灰度图，然后根据灰度将每个像素替换成不同的字符，将得到的字符串输出到文本文件中，打开就会看到酷酷的字符画了。（我使用的方程是 gray = int(0.2126\*r + 0.7152\*g + 0.0722\*b)）


#### 人脑的图片格式？
视网膜所获取，在大脑内形成的图像，是连续的还是离散的呢？它能无限放大吗？它有像素点吗？


### *8 wordcloud词云库
wordcloud很简单，只有三个对象：WordCloud，ImageColorGenerator，random_color_func。

如何生成一个词云呢？    
输入：      
1. 文本或整理好的词频dict
2. 背景轮廓
3. 染色方式
4. 词的格式：字体、大小

输出：  
词云图片


##### WordCloud生成
WordCloud是最重要的对象。绝大部分的参数设置在初始化时完成。

WordCloud(  font_path , width, height, mask, min_font_size, max_font_size , max_words = int, stopwords = set of strings, background_color=color value, mode, color_func, colormap  )    
参数|作用
---|---
font_path|字体的地址。      
mask = nd-array|标注能够放置词语的位置的二进制数组。       
min_font_size, max_font_size|字体大小限制      
max_words|数量限制     
stopwords = set of strings|停止词，即忽略掉的词        
background_color=color value|默认背景颜色      
color_func, colormap|同recolor     

##### mask使用图片的轮廓
需要使用matplotlib.pyplot库。
```python
backgroud_Image = plt.imread('path')
wc = WordCloud(mask = backgroud_Image) 
```
或者使用numpy+PIL库
```python
alice_mask = numpy.array(Image.open('path'))
# ...
```

##### 生成词云
|方法|使用|
---|---
generate(text) |generate_from_frequencies( process_text(text) )    
generate_from_frequencies(frequencies)|freq是一个dict(str,float)  
process_text(text)| 切分字符串并且统计词频，返回词频dict，省略掉一个字的词和停止词表里的词。这里的切分是用正则表达式切分的，功能强大，空格和/都能识别。

##### 染色        
recolor(self, random_state=None, color_func=None, colormap=None) 

colormap暂时不能理解是什么。和matplotlib的colormap类型很相关，似乎是个数值映射的类型。
wordcloud库的另外两个对象ImageColorGenerator(image)，random_color_func()两个对象都是用来染色的对象，直接当做color_func使用。

##### 保存
to_file(filename)

##### 输出到屏幕
需要使用matplotlib.pyplot库
```python
# 显示词云图
plt.imshow(wc)
# 是否显示x轴、y轴下标
plt.axis('off')
plt.show()
```

##### 使用经验
如何使词云效果更好？
1. 背景图片要结构简单易于识别背景。分辨率尽量高。
2. 颜色黑底白字对比度最好
3. 最小字体10-15，最大字体应该是图片高度的1/10

##### mac os字体位置
1. /System/Library/Fonts路径下（中文字体路径）
2. /Library/Fonts路径下

[常见字体名称](https://www.cnblogs.com/shuaixf/archive/2014/01/18/3525279.html)

mac os中文常用：
华文黑体 /System/Library/Fonts/STHeiti Medium.ttc 

### *9 json库

| |dict/list of dict -> .json | .json -> dict/list of dict
---|---|---
string | dumps(obj, sort_keys=False, indent=None) | loads(string)
file |dump(obj, fp, sort_keys=False, indent=None) | load(fp)

