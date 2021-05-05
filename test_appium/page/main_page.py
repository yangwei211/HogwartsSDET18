# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/24 4:18 下午
@file: main_page.py
@desc: 
"""
# 主页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.base_page import BasePage
from test_appium.page.contactlist_page import ContactListPage


class MainPage(BasePage):
    contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")


    def goto_contactList(self):

        # click 通讯录
        self.find(*self.contact_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactListPage(self.driver)
