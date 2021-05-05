# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/27 11:39 下午
@file: base_page.py
@desc: 
"""
# 基类，init
# 封装一些最基本的方法,便于后续维护
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging


logging.basicConfig(level=logging.INFO)

class BasePage:

    def __init__(self, driver: WebDriver=None):
        # 初始化driver
        self.driver = driver

    def find(self, by, value):
        logging.info(by)
        logging.info(value)
        # 查找元素
        return self.driver.find_element(by, value)

    def swipe_find(self ,text ,num = 5):

        self.driver.implicitly_wait(1)
        for i in range(0 ,num):

            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except NoSuchElementException:
                print("未找到，滑动")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num -1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{i}次，未找到")