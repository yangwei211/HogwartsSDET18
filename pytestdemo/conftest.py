# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/11 3:02 下午
@file: conftest.py
@desc: 
"""
from typing import List

import pytest

from Calculator import Calculator


@pytest.fixture()
def connectDb():
    # 相当于setuo
    print("连接数据库操作")
    # return "database datas"
    yield "搜索结果"  # 返回后面的结果 相当于return
    # 相当于teardown
    print("断开数据库连接")


@pytest.fixture()
def login():
    print("login")
    username = "hogwarts"
    password = "123"
    return username, password


@pytest.fixture(scope='class')
def initcalc_class():
    # setup
    print("setup")
    calc = Calculator()
    yield calc  # retutrn 记录上一次执行的结果，下次调用的时候，直接执行后面的动作
    # teardown
    print("teardown")


def pytest_collection_modifyitems(session, config, items: List):
    print("这是收集所有的测试方法")
    print(items)
    # items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
