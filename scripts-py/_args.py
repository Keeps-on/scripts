# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 18:22
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : _args.py


# *args的使用方法
# *args 用来将参数打包成tuple给函数体调用

def foo(*args):
    print(args, type(args))


foo(1)  # (1,)  <class 'tuple'>


def bar(x, y, *args):
    print(x, y, args)
    print(args[0])  # 使用索引


bar(1, 2, 3, 4, 5)  # 1 2 (3, 4, 5)


# **kwargs的使用方法
# **kwargs 打包关键字参数成dict给函数体调用

def func(**kwargs):
    print(kwargs, type(kwargs))


func(a=2)  # {'a': 2} <class 'dict'>


def function(**kwargs):
    print(kwargs)


function(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}


def function1(arg, *args, **kwargs):
    print(arg, args, kwargs)


function1(6, 7, 8, 9, a=1, b=2, c=3)  # 6 (7, 8, 9) {'a': 1, 'b': 2, 'c': 3}
