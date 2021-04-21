# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/11 3:02 下午
@file: conftest.py
@desc: 
"""
import pytest


@pytest.fixture()
def connectDb():
    # 相当于setuo
    print("连接数据库操作")
    # return "database datas"
    yield "搜索结果"   # 返回后面的结果 相当于return
    # 相当于teardown
    print("断开数据库连接")


@pytest.fixture()
def login():
    print("login")
    username = "hogwarts"
    password = "123"
    return username, password