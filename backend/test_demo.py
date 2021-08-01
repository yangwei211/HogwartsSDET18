# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/7/13 10:36 上午
@file: test_demo.py
@desc: 
"""
import requests

def test_req():
    data = {"a":1,"b":2 }
    r = requests.post('http://127.0.0.1:8000/',json=data)
    print(r.json())