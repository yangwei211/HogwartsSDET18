# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/30 12:06 上午
@file: contactinfo_page.py
@desc: 
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class ContactInfoPage(BasePage):

    def delete_contact(self):
        sleep(1)
        self.find(MobileBy.XPATH,"//android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView").click()
        self.find(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        self.swipe_find('删除成员').click()
        self.find(MobileBy.XPATH,"//*[@text='确定']").click()
        self.find(MobileBy.XPATH,"//*[@text='通讯录']")
        sleep(1)