# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/18 2:47 下午
@file: add_member.py
@desc: 
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_web_wechat.page.base_page import BasePage
from test_web_wechat.page.contact import ContactPage


class AddMemberPage(BasePage):
    # 设定为元组
    # 页面元素不需要让业务用例了解,所以要加私有
    __ele_username = (By.ID, "username")
    __ele_accid = (By.ID, "memberAdd_acctid")
    __ele_phone = (By.ID, "memberAdd_phone")

    def add_member(self, username, accid, phone):
        # *的作用是解元组 self.driver.find_element(*username) 等同于
        # self.driver.find_element(By.ID,"username")
        self.driver.find_element(*self.__ele_username).send_keys(username)
        self.driver.find_element(*self.__ele_accid).send_keys(accid)
        self.driver.find_element(*self.__ele_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(3)
        # 页面的return 分成两个部分
        # 1.其他页面的 实例
        # 2.用例所需要的断言
        # 注意：不要写成ContactPage
        return ContactPage(self.driver)

    def add_member_fail(self, username, accid, phone):
        # self.driver.find_element(*self.ele_username).send_keys(username)
        self.find(self.__ele_username).send_keys(username)
        self.driver.find_element(*self.__ele_accid).send_keys(accid)
        self.driver.find_element(*self.__ele_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        element = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = []
        for ele in element:
            error_list.append(ele.text)
        return error_list



    def add_xxx(self):
        # 调用本身的实例
        # AddMemberPage()
        return self
