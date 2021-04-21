# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/18 10:02 上午
@file: conftest.py
@desc: 
"""
import pytest


@pytest.fixture()
def login():
    print("这是企业微信的登录")