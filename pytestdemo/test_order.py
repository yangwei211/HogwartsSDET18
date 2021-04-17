# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/11 4:16 下午
@file: test_order.py
@desc: 
"""
import pytest
from selenium import webdriver


@pytest.mark.second
def test_one():
    print("one")


@pytest.mark.last
def test_last():
    print("laast")


@pytest.mark.first
def test_two():
    print("two")


def test_demo():
    driver = webdriver.Chrome()
    driver.get("www.baidu.com")