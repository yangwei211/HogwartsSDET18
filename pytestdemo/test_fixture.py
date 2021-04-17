# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/11 2:39 下午
@file: test_fixtture.py
@desc: 
"""
import pytest

# @pytest.fixture(scope="module")
# def a():
#     print("测试auto")


def test_search(connectDb):
    print(connectDb)
    print("搜索")


@pytest.mark.usefixtures('connectDb')
def test_add_cart():
    print("添加购物车")


def test_order(login):
    print("订单")
