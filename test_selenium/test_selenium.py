# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/15 10:17 下午
@file: test_selenium.py
@desc: 
"""
from time import sleep

import selenium
from selenium import webdriver


def test_demo():

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    sleep(3)
