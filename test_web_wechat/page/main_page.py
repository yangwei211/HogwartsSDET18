# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/18 2:47 下午
@file: main_page.py
@desc: 
"""
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_wechat.page.add_member import AddMemberPage
from test_web_wechat.page.base_page import BasePage
from test_web_wechat.page.contact import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        """
        跳转到通讯录
        :return:
        """
        sleep(3)
        self.driver.find_element(By.ID,"menu_contacts").click()
        sleep(2)
        return ContactPage(self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """

        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()
        sleep(2)

        # 返回要跳转页面的实例对象
        return AddMemberPage(self.driver)