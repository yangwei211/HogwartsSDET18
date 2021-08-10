# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/10 3:39 下午
@file: test_setup_teardown.py
@desc: 
"""


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_case1():
    print("case1")

class TestDemo1:
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")


    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")















