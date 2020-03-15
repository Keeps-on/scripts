# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:22
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : _re.py

import re

"""
########### 修饰符 ############
re.I 使匹配对大小写不敏感
re.L 做本地化识别匹配
re.M 多行匹配,影响^和$
re.S 使.匹配包括换行在内的所有字符
re.U 根据Unicode字符集解析字符.这个标志影响\w \W \b \B
re.X 该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解.
# 模式
########### 字符 ###############
^ 匹配字符串开头
$ 匹配字符串结尾
. 匹配人以字符,除了换行符号.当re.DOTAALL标记被指定时,则可以匹配包括换行符的任意字符.
[...] 用来表示一组字符,单独列出:[amk]匹配a,m或k
[^...] 不在[]中的字符:[^amk]匹配除amk之外的字符

* 匹配0个或多个的表达式
+ 匹配1个或多个的表达式
? 匹配0个或1个由前面的正则表达式定义的片段,非贪婪方式.
{n} 精准匹配n个前面表达式
{n,} 匹配大于等于n个前面表达式
{n,m} 匹配n到m个前面的表达式定义的片段,贪婪方式

a|b 匹配a或b
(...) 对正则表达式分组,并记住匹配的文本
(?imx) 正则表达式包含三种可选标志,imx,只影响括号中的区域.
(?-imx) 正则表达式关闭imx可选标志,只影响括号中的区域.
(?:re) 类似(...)但不表示一个组
(?imx:re) 在括号中使用imx可选标志
(?-imx:re) 在括号中不是用imx可选标志
(?#...) 注释
(?=re) 前向肯定界定符.如果所含正则表达式,以...表示,在当前位置成功匹配时成功,否则失败.但一旦所含表达式已经尝试,匹配引擎根本没有提高,模式的剩余部分还要尝试界定符右边.
(?!re) 前向否定界定符.与肯定界定符相反;当所含的表达式不能在字符串当前位置匹配成功时成功.
(?>re) 匹配的独立模式,省去回朔.
\w 匹配字符数字以及下划线
\W 匹配非字母数字下划线
\s 匹配任意空白字符,等价于[\t\n\r\f]
\S 匹配任意非空白字符
\d 匹配任意数字
\D 匹配任意非数字
\A 匹配字符串开始
\Z 匹配字符串结束,如果是存在换行,只匹配到换行前的结束字符串.
\z 匹配字符串结束
\G 匹配最后匹配完成的位置
\b 匹配一个单词边界,也就是指单词和空格之间的位置
\B 匹配非单词边界
\n \t 匹配一个换行符,一个制表符
\1...\9 匹配第n个分组的内容


https://www.cnblogs.com/aylin/p/5516430.html

https://blog.csdn.net/lijunweiyhn/article/details/85105255

https://www.jb51.net/article/166398.htm

https://www.jb51.net/article/166398.htm

https://www.cnblogs.com/CYHISTW/p/11363209.html

"""

#############################
#      re.match()           #

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# 语法
# re.match(pattern, string, flags=0)
# 参数
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见上方可选标志表格

print(re.match('www', 'www.baidu.com').span())  # (0, 3) 注意从开头开始匹配
print(re.match('baidu', 'www.baidu.com'))  # None

#############################
#      re.search()           #

# re.search 扫描整个字符串并返回第一个成功的匹配。
# 语法
# re.search(pattern, string, flags=0)
# pattern	  匹配的正则表达式
# string	  要匹配的字符串。
# flags	      标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见上方可选标志表格

match_obj1 = re.search('www', 'www.baidu.com')
match_obj2 = re.search('baidu', 'www.baidu.com')

print(match_obj1)  # <_sre.SRE_Match object; span=(0, 3), match='www'>
print(match_obj1.span())  # (0, 3)
print(match_obj1.group())  # www
print(match_obj1.groups())  # ()

#############################
#      re.compile()         #

# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# 提前编译可减少多次正则匹配的运行时间
# re.compile(pattern[, flags])
# 参数
# pattern : 一个字符串形式的正则表达式
# flags 可选，表示匹配模式
# 由于Python的字符串本身也用\转义，所以要特别注意：

s = 'ABC\\-001'  # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'
# 因此建议使用Python的r前缀，就不用考虑转义的问题了：
s = r'ABC\-001'  # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息
    print(match.group())

#############################
#      re.findall()         #
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。
# 语法格式为：
# re.findall(string, pos, endpos)
# 参数：
# string 待匹配的字符串。
# pos 可选参数，指定字符串的起始位置，默认为 0。
# endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。

mat = re.compile(r'\d+')  # 匹配数字
print(mat.findall('abafa 124ddwa56'))  # ['124', '56']
print(mat.findall('abafa 124ddwa56', 0, 7))  # 匹配从0位开始，到7位结束 ['1']
#############################
#     re.finditer()        #
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
# 语法
# re.finditer(pattern, string, flags=0)
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
"""
12
32
43
3
"""
##############################
#     re.split()             #
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
# 语法
# re.split(pattern, string[, maxsplit=0, flags=0])
# 参数
# pattern	  匹配的正则表达式
# string	  要匹配的字符串。
# maxsplit	  分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags   	  标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见上方可选标志表格


res = re.split(r'\s+', 'a b   c')
print(res)  # ['a', 'b', 'c']

res2 = re.split(r'[\s\,]+', 'a,b, c  d')
print(res2)  # ['a', 'b', 'c', 'd']

res3 = re.split(r'[\s\,\;]+', 'a,b;; c  d')
print(res3)  # ['a', 'b', 'c', 'd']

##############################
#         re.sub()          #
# Python 的re模块提供了re.sub用于替换字符串中的匹配项。
# 语法
# re.sub(pattern, repl, string, count=0, flags=0)
# 参数：
# pattern :   正则中的模式字符串。
# repl :      替换的字符串，也可为一个函数。
# string :    要被查找替换的原始字符串。
# count :     模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# flags :     编译时用的匹配模式，数字形式。

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)


# repl 参数可以是一个函数
# 以下实例中将字符串中的匹配的数字乘于 2：
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
# A46G8HFD1134
