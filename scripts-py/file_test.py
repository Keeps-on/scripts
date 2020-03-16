#-*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:22
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : file_test.py 

####################################
#          Python操作文件
####################################

############## 读文件 ##############
# 打开一个文件用open()方法 --- > 文件对象(可迭代)

f = open('file_test.txt','r')
print(f) # <_io.TextIOWrapper name='file_test.txt' mode='r' encoding='UTF-8'>
f.close() # 将文件关闭
"""
r  表示文本文件(默认值)
rb 表示二进制文件
如果文件不存在，open会抛出一个IOError的错误
由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
"""
try:
  f = open('file_test.txt','r')
  print(f.read())
finally:
  print("文件已关闭")
  if f:
      f.close()
####################################
#    with open 自动关闭文件
####################################

with open('file_test.txt','rb') as f: # 使用rb的方式进行读取文件
    print(f.read())


####################################
#   三种读取文件的方式 
####################################

# read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。如果文件大于可用内存，为了保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。.readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
# readline() 每次只读取一行，通常比readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 readline()。
# 注意：这三种方法是把每行末尾的'\n'也读进来了，它并不会默认的把'\n'去掉，需要我们手动去掉。
with open('file_test.txt','r') as f:
    file_list = f.readlines()
    print(file_list)
for i in range(0,len(file_list)):
    file_list[i] = file_list[i].rstrip('\n')
    print(file_list)
    

with open('file_test.txt','r') as f:
    line = f.readline()
    print(line)


############## 写文件 ##############
f = open('file_test.txt','w') # wb 表示二进制读写
f.write('Hello world!')
f.close()
# 注意：
#  w 表示清空写并且当文件不存在的时候会创建该文件(存在：清空写)
#    当不想清空原来的内容而是直接在后面追加新的内容，就是用 a 的模式

#    我们可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
#    当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，
#    空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数
#    据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的
#    丢失了。所以，还是用with语句来得保险：
#    python文件对象提供了两个“写”方法： write() 和 writelines()。
#    write()方法和read()、readline()方法对应，是将字符串写入到文件中。
#    writelines()方法和readlines()方法对应，也是针对列表的操作。它接收一个字符串列表作为参数，
#    将他们写入到文件中，换行符不会自动的加入，因此，需要显式的加入换行符。
f1 = open('test1.txt', 'w')
f1.writelines(["1", "2", "3"])
#    此时test1.txt的内容为:123

f1 = open('test1.txt', 'w')
f1.writelines(["1\n", "2\n", "3\n"])
#    此时test1.txt的内容为:
#    1
#    2        
#    3


# 关于open()的mode参数：
#
# 'r'：读
#
# 'w'：写
#
# 'a'：追加
#
# 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）
#
# 'w+' == w+r（可读可写，文件若不存在就创建）
#
# 'a+' ==a+r（可追加可写，文件若不存在就创建）
#
# 对应的，如果是二进制文件，就都加一个b就好啦：
#
# 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
#























# https://www.cnblogs.com/zyber/p/9578240.html

