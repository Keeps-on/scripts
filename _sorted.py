# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 15:20
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : sorted.py

"""
问题 ： 根据字典中的某一列进行排序

由小到大排序
新列表 = sorted(列表，key=lambda 形参：形参[str键名称])
由大到小排序
新列表 = sorted(列表，key=lambda 形参：形参[str键名称], reverse = True)

"""
data = [
    {"index": 1, "name": "孙悟空"},
    {"index": 5, "name": "猪八戒"},
    {"index": 13, "name": "沙和尚"},
    {"index": 10, "name": "唐僧"}
]

filter_data = sorted(data, key=lambda d: d["index"])
print(filter_data)
"""
[{'index': 1, 'name': '孙悟空'}, {'index': 5, 'name': '猪八戒'}, {'index': 10, 'name': '唐僧'}, {'index': 13, 'name': '沙和尚'}]
"""
