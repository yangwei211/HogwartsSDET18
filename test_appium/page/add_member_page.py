# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/24 4:20 下午
@file: add_member_page.py
@desc: 
"""
# from test_appium.page.edit_member_page import EditMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.base_page import BasePage


class AddMemberPage(BasePage):



    def addmember_bymenual(self):
        # click 手动输入添加
        from test_appium.page.edit_member_page import EditMemberPage
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditMemberPage(self.driver)

    def find_tost(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
