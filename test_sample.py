# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/8 11:48 下午
@file: test_sample.py
@desc: 
"""
import pytest
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5