# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/16 12:27 下午
@file: test_3.py
@desc: 
"""
import requests

# r = requests.get("http://www.baidu.com")
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# print(r.text)
print(r.json())











