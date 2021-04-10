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


@pytest.mark.login
def test_answer():
    assert func(4) == 5
