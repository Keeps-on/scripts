# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 8:21
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : _os.py 
# @参考  :


import os

# 获取当前的工作目录
current_path = os.getcwd()
print(current_path)
# 改变当前脚本工作目录;相当于shell cd
# change_path = os.chdir('/home/test.sh')
print(os.getcwd())
# 返回当前目录 .
print(os.curdir)
# 返回上级目录 ..
print(os.pardir)
# 生成多层递归目录
# print(os.makedirs('dirname1/dirname2'))
# 创建目录
os.mkdir('dirname')
# 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.rmdir('dirname'))
# 返回path指定的文件夹包含的文件或文件夹的名字的列表。
os.listdir('path')
## os.path模块
# 返回绝对路径
os.path.abspath("/etc/sysconfig/selinux")
# 返回文件名--selinux
os.path.basename("/etc/sysconfig/selinux")
# 返回一个目录的目录名--/etc/sysconfig
os.path.dirname("/etc/sysconfig/selinux")
# 如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
os.path.exists("/home/egon")  # False
os.path.exists("/root")  # True
# 判断是否为绝对路径
os.path.isabs("/root")  # True
# 测试指定参数是否是目录名
os.path.isdir("/etc/sysconfig/selinux")  # False
os.path.isdir("/etc/sysconfig/")  # True
# 测试指定参数是否是一个文件
os.path.isfile("/etc/sysconfig/selinux")  # True
# 将目录名和文件的基名拼接成一个完整的路径
os.path.join("/home/code/scripts","email.py")
# 分割目录名，返回由其目录名和基名给成的元组
os.path.split("/home/code/scripts/email.py") # ('/home/code/scripts', 'email.py')
# 分割文件名，返回由文件名和扩展名组成的元组
os.path.splitext("/home/code/scripts/email.py") # ('/home/code/scripts/email', '.py')
