# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/10 2:07 下午
@file: sample_test.py
@desc: 
"""
import pytest


def func(x):
    return x + 1

@pytest.mark.search
def test_answer():
    assert func(3) == 5