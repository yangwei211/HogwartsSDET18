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

@pytest.fixture(params=[['tom',123],['jerry',456]],
                ids=['tom','jerry'])
def login(request):
    # request是固定的写法，request.param也是固定写法
    return request.param
    # print(request.param)
    # print("login")

# fixture提供给测试用例参数
def test_login(login):
    print(login)
