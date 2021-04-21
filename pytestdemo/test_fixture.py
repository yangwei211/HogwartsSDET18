# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/11 2:39 下午
@file: test_fixtture.py
@desc: 
"""
import pytest

# module 模块级别
# @pytest.fixture(scope="module")
# def a():
#     print("测试auto")





# @pytest.mark.usefixtures('connectDb')
def test_search(connectDb):
    print(connectDb)
    print("搜索")



def test_add_cart():
    print("添加购物车")


def test_order(login, connectDb):
    username, password = login
    print(username, password)
    print("订单")
