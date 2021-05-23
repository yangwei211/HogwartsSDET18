# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/7 11:11 下午
@file: time_标准库urllib.py
@desc: 
"""
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')

# print(response.status)
# print(response.read())
print(response.headers)
























