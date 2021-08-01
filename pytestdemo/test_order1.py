# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/6/9 10:43 下午
@file: test_order1.py
@desc: 
"""
import pytest


@pytest.mark.run(order=3)
def test_order():
    print("cccc")



