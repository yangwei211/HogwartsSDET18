# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/27 10:24 下午
@file: edit_member_page.py
@desc: 
"""
# from test_appium.page.add_member_page import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.page.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phonenum):
        # input name
        # input phonenum
        # click 保存
        from test_appium.page.add_member_page import AddMemberPage
        self.find(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(
            phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        return AddMemberPage(self.driver)
