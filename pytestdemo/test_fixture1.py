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
                ids=['tom','jerry']
                )
def login(request):
    return request.param
    # print("login")


def test_login(login):
    print(login)
