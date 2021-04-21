# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/18 4:12 下午
@file: base_page.py
@desc: 
"""
from time import sleep

import yaml
from selenium import webdriver


class BasePage:

    """
    把重复的步骤抽离出来，封装，比如driver实例化
    """
    # 没有参数传入，会取默认的None，如果有参数传入，会取传入的参数
    def __init__(self, base_driver=None):
        """
        driver 重复实例化会导致页面多次启动
        解决driver 重复实例化的问题
        :param base_driver:
        """
        if base_driver == None:
            # 实例化 driver
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            with open("data.yaml",encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐身等待，每一次调用find方法
            self.driver.implicitly_wait(3)
        else:
            self.driver = base_driver

    def find(self, by, ele = None):
        """

        :param by:定位方式css ,xpath, id
        :param ele: 元素定位信息
        :return:
        """
        # 两种传入定位元素的方式，提高代码的兼容性
        # 如果传入的是元组，那就只有一个参数
        if ele is None:
            return  self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)