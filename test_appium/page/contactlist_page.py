# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/24 4:20 下午
@file: contactlist_page.py
@desc: 
"""
from appium.webdriver.common import mobileby
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from test_appium.page.add_member_page import AddMemberPage
from test_appium.page.base_page import BasePage
from test_appium.page.contactinfo_page import ContactInfoPage


class ContactListPage(BasePage):

    def goto_addmember(self):
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_contactinfo(self):
        self.find(MobileBy.XPATH,"//android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView").click()
        return ContactInfoPage(self.driver)