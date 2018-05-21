#!user/bin/python3
#Author:Mr.Yuan
#-*- coding:utf-8 -*-
#@time: 2018/5/17 14:29
# 1、常用字符串格式化有哪些?并说明他们的区别
#format()  这个我个人认为是最灵活的可以传所有的数据类型不仅限于字符串，可以使元祖，字典，列表等等，适用任意场景
# %s       这个是最常用的格式化输出，但是传入的对应占位符的数据类型只能是字符串
# %d       传入的对应占位符的数据类型只能是数字类型，并且是整形
# %r       传入的对应占位符的数据类型只能是字符串，并且输出的占位符所在位置的字符串是带引号的
# 2、请手写一个单例模式（面试题）
# class A:
#     __instance = None
#     def __init__(self):

# 3、利用 python 打印前一天的本地时间，格式为‘2018-01-30’（面试题）
# import time
# now_time = time.time()
# old_time  = now_time - 24*60*60
# ret =time.localtime(old_time)
# ret = time.strftime('%Y-%m-%d',ret)
# print(ret)
# 4、python 中 search()和 match()的区别(面试题)
#   search  是匹配目标字符串中的第一个符合要求的字符
#   match   是匹配目标字符串的第一个字符是否符合要求
# 5、写一个闭包函数 clo，接收整数参数 n ，返回一个函数 foo，foo 函数的功能是把 foo 参数和 n 相乘并把结果返回。
# def clo(n):
#     def foo(m):
#         return n*m
#     return foo
# print(clo(12)(3))
# 6、# 取出 html 中的歌手名和歌名
# ᨀ示：
# <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
# html = '''<div id="songs-list">
#  <h2 class="title">经典老歌</h2>
#  <p class="introduction">
#  经典老歌列表
#  </p>
#  <ul id="list" class="list-group">
#  <li data-view="2">一路上有你</li>
#  <li data-view="7">
#  <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#  </li>
#  <li data-view="4" class="active">
#  <a href="/3.mp3" singer="齐秦">往事随风</a>
#  </li>
#  <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#  <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#  <li data-view="5">
#  <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
#  </li>
#  </ul>
# </div>'''
# import re
# music = re.findall(r'singer=(.*)</a>',html)
# music_singer = []
# for i in  music:
#     i = i.replace('>','|').strip()
#     music_singer.append(i)
# print(music_singer)

# 7、请写出函数式编程 filter、map 的实例。
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]过滤出列表的所有奇数(filter)
# [1,2,3,4,5]计算出每个元素的平方(map)
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_l =filter(lambda x:x%2==1,l)
# for i in new_l:print(i)
# l1 = [1,2,3,4,5]
# new_l1 = map(lambda x:x**2,l1)
# for i in new_l1:print(i)
# 8、简述 Python 垃圾回收机制
#首先在python中一切皆对象，在python解释器中每新建一个对象就会对这个对象起一个计数器，每当这个对象被引用一次，这个计数器就会加1，而当你python解释器内部每隔一段时间你
# 不去调用这个变量，这个计数器就会相应减1，若你在一定的时间内一直没用这个对象，这个计数器减为了0，那么这个对象就会被回收。
# 9、用最简洁的方式生成这样一个列表【4，16，32，64，128】
# li = [2**n  for n in range(2,8) if n!=3]
# print(li)
# 10、简述 python GIL 的概念， 以及它对 python 多线程的影响?。
# pthon的GIL就是python的全局解释器锁，这个锁只存在cpython的解释器中。
# 影响：在多计算的python程序中，导致不能够开启多线程，因为在同一时刻只能有一个线程去访问用一个CPU。
# 11、写一段程序逐行读取一个文本，并在屏幕上输出
# with open('file_name',encoding='utf-8') as f :
#     while True:
#         try:
#             content = f.readline()
#             print(content)
#         except Exception:
#             break

# 12、如何用 Python 删除一个文件,创建一个文件夹
# import os
# os.remove('filename')  删除文件
# os.mkdir()   普通创建
# os.makedirs()可以递归创建文件夹
# 13、什么是”并发“？什么是”并行“？
#并发是同时开启多个进程，但是不运行
#并行是同时又多个进程在运行
# 14、᧿述 Event 的执行机制
#Event 的执行机制：wait的时候，如果事件.is_set 为True则事件代正常往下执行，否则就阻塞，可以通过clear和set来改变时间的状态。
# 15、什么是粘包，如何避免？
#首先黏包只存在于tcp协议中。
#造成黏包最最最主要的原因就是客户端对接受的到的消息不知道从哪里断句。
# 黏包就是在客户端在发送消息时，消息过长(消息过短，且两次发送的时间间隔很短是另外一种情况，也会造成黏包)时，由于客户端要解包，就造成了客户端接受到了不完整的消息，
# 而客户端又不知道服务端发送的消息究竟有多大，就就会造成客户端收到的消息可能不完整，甚至是接受的消息还包含有上一条服务端发送过来的消息
#如何解决：通过strcut这个模块来解决，把我要传送的消息放在一个字典中，字典中包含我将要发送的消息的长度。把这个字典同伙struct模块转化成一个定长的bytes传过去给客户端，
         # 客户端通过这个字典里面的信息，就可以准确的知道接下来要接受的信息的长度。
# 16、叙述 TCP、UDP 的区别
# 1，tcp协议传输效益更加安全，udp是面向信息流的消息传递方式所以接受和传输不安全。
# 2，tcp协议只客户端与服务端只能一对一建立连接，比较占空间。udp的服务端可以一对多建立连接更省空间
# 3，tcp建立和断开有三次握手和四次挥手，而udp协议没有
# 17、叙述 OSI 七层协议是什么，三次握手，四次挥手分别是什么
#应用层，传输层，网络成，数据链路层，物理层
#三次握手：
#        第一次：就是tcp协议的服务端与客户端建立连接时，服务端首先要去跟客户端建立连接这时候要给客户端发送一条消息告知客户端
#          第二次：客户端收到服务端发送的连接请求可，客户端也给服务端发送一条消息告知服务端我准备好了。
#          第三次：服务端收到客户端的会用之后就开始于客户端建立连接发并送消息。
#四次挥手：
       # 第一次： tcp下一服务端先发送一条消息告诉客户端我要和你断开连接
       # 第二次： 客户端收到服务端发送来的消息后 对服务端的断开请求做出回应发送一条消息
       #第三次：客户端这时候还要问下服务端还有没有别的消息要发送的(事实上这里是由于TCP协议的半关闭原则造成的，是为了防止有的消息发送了一半没有发送完)所以又发送了一条消息
       #第四次：服务端收到消息后，确认了没有消息要发送了，或者是所有的消息的发送完了，就回了一条消息给客户端，这时候就断开了连接
# 18、简述你对管道、队列的理解；
    # 队列 ： 利用了管道和锁，先进先出、数据进程更加安全
# 管道
    # 双向通信 也就是双工，数据进程不安全
# 19、编程题；写一个装饰器实现功能:打印程序的运行时间
# def wrapper(func):
#     def inner(*args,**kwargs):
#         '''被装饰函数之前'''
#         ret = func(*args,**kwargs)
#         '''被装饰函数之后'''
#         return ret
#     return inner
#
# @wrapper
# def func(a,b):
#     pass
#     return 566
# import time
# def timmer(func):
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         ret = func(*args,**kwargs)
#         time.sleep(0.3)#模拟程序运行时间
#         end_time = time.time()
#         print('此函数的执行效率%s' % (end_time - start_time))
#         return ret
#     return inner
# @timmer
# def func():
#     pass
# func()
# 20、写一个简单的 Python socket 服务端和客户端
# import socket
# s = socket.socket()
# id_port = ('127.0.0.1',8000)
# s.bind(id_port)
# s.listen()
# conn,addr =s.accept()
# date = conn.recv(1024)
# print(date.decode('utf-8'))
# conn.send('hello'.encode('utf-8'))
# conn.close()
# s.close()
#
# import socket
# s = socket.socket()
# id_port = ('127.0.0.1',8000)
# s.connect(id_port)
# s.send('你好'.encode('utf-8'))
# date = s.recv(1024)
# print(date.decode('utf-8'))
# s.close()

# 21、使用 python 简单实现打印九九乘法表
# 优化版：使用一行代码实现九九乘法表
# l = [i for i in range(1,10)]
# # print(l)
# for i in range(len(l)):
#     l2 = [l[i]*n for n  in range(1,l[i]+1)]
#     print(l2)
# 22、 请找出以下代码的问题。ᨀ示：5 处
# 1. #Python3 环境
# 2. class dummyclass(object):
# 3. def __init__(self):
# 4. self.is_d = True
# 5. pass
# 6.
# 7. class childdummyclass(dummyclass):
# 8. def __init__(self, isman):
# 9. self.isman = isman
# 10.
# 11. @classmethod
# 12. def can_speak(self): return True
# 13.
# 14. @property
# 15. def man(self): return self.isman
# 16.
# 17. if __name__ == "__main__":
# 18. object = new childdummyclass(True)
# 19. print object.can_speak()
# 20. print object.man()
# 21. print object.is_d
# 错误1。两个类的首字母没有大写
#    2。创建对象的时候，也就是实例化的时候，类名不对new childdummyclass  没有这个类名
#    3.python3默认所有的类都是新式类，默认继承obect类，所以没必要这么写class dummyclass(object)
#    4.print object.can_speak()  这个can_speak为类方法，调用方式为类名加方法名
#    5.print object.man()   这个方法调用了@property  把方法伪装成了属性，所以在调用的时候不用加括号
# 23、爬虫程序中有如下代理池，请随机选择一个代理。
# PROXIES = [
#  {'ip_port': '111,11,221,32:80', 'user_pass': ''},
#  {'ip_port': '12.75.44.55:8120', 'user_pass': ''},
#  {'ip_port': '64.34.11.22:3330', 'user_pass': ''},
#  {'ip_port': '64.23.4.11:1025', 'user_pass': ''},
#  {'ip_port': '55.31.121.11:80', 'user_pass': ''},
# ]
# import random
# id = PROXIES[random.randint(0,(len(PROXIES)))-1]
# print(id)
# 24、编写程序输入一个字符串，返回倒叙的结果，如:’abcdef’，返回’fedcba’
# s = 'abcdef'
# s1 = s[-1:0:-1]
# print(s1)
# 25、编程题
# """
# 一：定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回 3 门科目中最高的分数。get_course() 返回类型:int
# class Student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.coursel = course
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_course(self):
#         return max(self.coursel)
# # 写好类以后，可以定义 2 个同学测试下:
# zm = Student('zhangming',20,[69,88,100])
# print(zm.get_course())
# print(zm.get_age())
# print(zm.get_name())
# 返回结果：
# zhangming
# 20
# 100
# """
# 26、᧿述多进程开发中 join 与 daemon。
#在多进程中 join是等待被join的子进程进程结束之后在进程程序的下一步
#daemon是守护进程的意思，被守护的子进程会随着主进程的代码的结束而结束。
# 27、什么是异步，什么是异步阻塞?
#异步就是两个互相关联的程序，一个可以一起执行，不用互相等待。
#异步阻塞就是两个互相关联的程序，一起执行之后，有一个先执行完了但是不能结束，因为另外一个程序还没有运行结束，这时候执行快的程序就因为执行慢的程序而阻塞了。就叫异步阻塞
# 28、写一个程序，包含十个线程，子线程必须等待主线程 sleep 10 秒钟之后才执行，并打印当前时间
# import time
# from threading import Thread
# def func(i):
#     print('*'*i)
# thread_lst = []
# time.sleep(10)
# for i in range(10):
#     t = Thread(target=func,args=(i,))
#     t.start()
#     thread_lst.append(t)
# for t in thread_lst:t.join()
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# # 29、请解释以下代码的输出结果。
# z = [lambda x:x*i for i in range(3)]
# for i in z:
#     print(i)
# x = [o(2) for o in z]
# print(x)
#因为z 最后的结果其实其实[lambda x:2x,lambda x:2x,lambda x:2x]
#而for o in  z 很明显每个o就是一个匿名函数，传参为2 所以每次的返回结果都为4  就是一个这样的列表[4, 4, 4]
# 30、写出程序，实现 socket 聊天并发实例，包含服务端、客户端
#服务端
from socket import *
from multiprocessing import Process

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)

def talk(conn,client_addr):
    while True:
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break

if __name__ == '__main__':
    while True:
        conn,client_addr=server.accept()
        p=Process(target=talk,args=(conn,client_addr))
        p.start()

# 31、叙述进程、线程、协程的区别
# 线程是cpu调度的最小单位 ，在同一进程中的线程数据共享、线程是在进程中的 一个执行单位
# 进程是资源分配的最小单位，进程程负责管理分配资源
#协程是线程的一个小分支，并且协程的开启没有数量限制。

# 32、
# class Foo:
#  country = '中国'
#  print(country)
#
#  def __init__(self,name,country):
#     self.name = name
#     self.country = country
#
# alex = Foo('alex','印度')
# Foo.country = '泰国'
# print(Foo.country)
# print(alex.country)
# 说出打印顺序和内容，并解释原因
#第一个中国是类中打印了类的静态属性
#第二个泰国是 Foo.country = '泰国'改变了类的静态属性打印print(Foo.country) 这时候为
#第三个印度  是对象alex的子集属性alex = Foo('alex','印度')  为印度