# 人人网好友关系图

恩，很大的题目，但做的很差。所以欢迎大家来fix
http://friend.renren.com/GetFriendList.do?curpage=0&id=xxx


## 更新
### 2020-01-08
1、安装Pydot
由于python位于usr下，故安装时不能使用sudo pip install pydot
我用了另外一种方式: sudo apt install python-pydot python-pydot-ng graphviz
发现深度os安装的pydot过旧，报错：ImportError: pydot 1.0.29 < 1.2.3
故覆盖安装指定版本：pip install pydot==1.2.3 --user



## 相关
https://github.com/snailrobert/some-spider.git

### 2020-01-12
python \uxxxx转中文
https://zhidao.baidu.com/question/938196078692953772.html

## python爬虫之xpath的基本使用
https://www.cnblogs.com/lei0213/p/7506130.html
https://www.cnblogs.com/xiaozx/p/10727164.html
https://www.cnblogs.com/lei0213/p/7506130.html

## python如何将xml对象转化为字符串（lxml）
https://blog.csdn.net/qq_40147863/article/details/82192119
https://blog.csdn.net/qq_38410428/article/details/82792730
https://blog.csdn.net/qq_37454841/article/details/80493994

## python爬虫系列--lxml（etree/parse/xpath)的使用
https://blog.csdn.net/qq_35208583/article/details/89041912

## Python自定义对象转json
https://blog.csdn.net/weixin_41431904/article/details/80733600
https://blog.csdn.net/u011304615/article/details/70140901
https://blog.csdn.net/helang296479893/article/details/83657309

### 2020-01-08

## Python参考网站
https://www.runoob.com/python/python-lists.html

python set元素访问
https://www.cnblogs.com/imhuanxi/p/11027555.html

Python返回数组（List）长度的方法
https://www.cnblogs.com/telwanggs/p/10383642.html

1、安装Pydot 由于python位于usr下，故安装时不能使用sudo pip install pydot 我用了另外一种方式: sudo apt install python-pydot python-pydot-ng graphviz 发现深度os安装的pydot过旧，报错：ImportError: pydot 1.0.29 < 1.2.3 故覆盖安装指定版本：pip install pydot==1.2.3 --user

解决ImportError: No module named pydot： 通常是pip install xxx

参考链接：
安装几个包：Keras网络训练可视化调用plot_model ，ImportError: Failed to import `pydot`.
networkx demo参考网站：https://www.cnblogs.com/wushaogui/p/9202853.html#53%E6%8C%87%E5%AE%9A%E8%BE%B9%E7%9A%84%E5%B1%9E%E6%80%A7
https://www.mlln.cn/2018/09/19/networkx%E5%85%A5%E9%97%A8/

Networkx参考手册
https://blog.csdn.net/qingqingpiaoguo/article/details/60570894

networkx相关API参考：
https://networkx.github.io/documentation/networkx-1.10/index.html
https://networkx.github.io/documentation/stable/reference/classes/graph.html#

networkx关于Graph的各种操作
https://blog.csdn.net/haoshan4783/article/details/90750456

Python: ValueError: too many values to unpack
https://www.cnblogs.com/baxianhua/p/8275627.html

Python中多层List展平为一层
https://www.cnblogs.com/wushaogui/p/9241931.html

TypeError: 'str' object does not support item assignment的原因
https://blog.csdn.net/eruituoa/article/details/82696387

gevent安装： sudo pip install gevent networkx lxml

sudo apt-get install graphviz


### 2013-03-03

使用 [graphviz](http://www.graphviz.org/) 绘图,
但还保留了 networkx，使用它来删除节点和计算degree

现在运行 `python local_graph.py` 就会生成一张漂亮的关系图（现在还没有在图上标记用户名）
所以请确保计算机一正确安装 graphviz

debian系用户只要简单的运行下面的命令即可

    sudo apt-get install graphviz
    



## 如何运行

1.  git clone 代码
2.  安装 requirements.txt中的依赖，建议virtualenv
3.  cp account.example account 然后按照其中格式填写人人网帐号
3.  python local_graph.py
    
    
    
运行程序，一段时间后（不同的网络环境会导致抓取时间差异很大，在我这里一共用了40分钟）
程序正常退出。就会在目录中生成一张 result.png 图片。

![renren_graphviz](http://i1297.photobucket.com/albums/ag23/yueyoum/result_zps1ff92b48.png)


**下面是用 networkx 和 matplotlib生成的图片，新代码默认不再使用**

![renren](http://i1297.photobucket.com/albums/ag23/yueyoum/renrenhaoyou_zps3d5d3845.png)


这是我校内好友的情况，可以看到这些好友明显是三个圈子：

*   高中同学圈子
*   大学同学圈子
*   码农圈子

还有一些孤立（不属于这三个大圈子的同学）的好友，没有显示。


## 初衷

初衷总是美好的，当我随便试了几个陌生人后，发现一样可以查看他们的好友。于是我就想到了
两个玩法：

1.  做一个网站，人们上来只要填写他的人人ID，就会动态的展现他的好友，好友之间的共同好友...
2.  在一个网站上输入两个人人ID，然后找出这两个ID之间的好友链。

最有意思的是第二个，因为我相信像人人网这样的强关系网络，以及大量的用户，两个用户之间
肯定会有一条/多条好友链接。

    端点 <-> A <-> B <-> C ...... X <-> Y <-> Z <-> 端点
    
当然这个也很难，没想到如何做，于是就做第一个想法。


## 美好的初衷是如何变成现在这个屌样的?

1.  某晚，正在在爬好友测试的时候，发现总是爬不到一些人的好友。
    然后才发现了一个悲剧的事实，（不过也是合理的）：
    
    **好友不是你想爬，想爬就能爬**
    
    只有开放了对应权限的才能察看其好友。
    
    这下好了，上面的想法2彻底做不了了。想法1也退化成只能自娱自乐了。
    也就是只能爬自己好友的好友了
    
    
2.  urllib2 怎么卡住呢？

    使用了gevent，我刚开始的模型是 对多个用户，以及同一个用户的好友，
    都利用gevent的并发来爬， 测试了两次后， urllib2 无法 read，
    到这里，一下卡住了。
    
    并发会卡住。顺序爬取很顺利，但太慢。
    后来偶然发现，
    
    **对同一个人不能并发的抓取， 但还可以对多个人并发**
    
    
3.  图太难看了

    本打算 angular.js + d3.js + gevent-socket.io 来动态的在web上绘图。
    但心急，想看看能绘制出什么样的图，于是先用 networkx 和 matplotlib 来绘图
    
    然后才发现 绘制好友的共同好友 几乎不可能，点全部重叠在一起，看都没法看……
    
    然后又一次吊丝的退化到只显示自己的好友
    
    最后还花了几小时来调节 图像的显示 效果。。。
    
    
## 可能遇到的问题


### 怎么无法登录？

请确保你有一个 account 文件，里面第一行写用户名/email， 第二行写password

如果在确保 account 文件正确的情况下，程序还是无法登录，请用浏览器登录一次，再运行程序

### 显示一个 collect friends 后怎么就卡住呢？

其实不是卡住了，只是抓取好友比较慢，这时又没有输出，所以看着像卡住了，请耐心等待

### 最后的图太简单了吧，有什么意思吗？

我也不想这样啊，蛋疼，欢迎你来增强它的功能和效果

### 程序跑完后会报一个这样错误： 

    `Exception KeyError: KeyError(17784656,) in ignored...`

这个直接忽略掉，应该是某个库不是线程安全的。但这个对结果没有影响。

    
