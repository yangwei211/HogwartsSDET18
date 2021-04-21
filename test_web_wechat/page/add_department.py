# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/21 10:22 下午
@file: add_department.py
@desc: 
"""
from selenium.webdriver.common.by import By

from test_web_wechat.page.base_page import BasePage


class AddDepartmentPage(BasePage):

    def add_department(self):

        self.driver.find_element(By.NAME,"name").send_keys("测试部门")
        self.driver.find_element(By.CSS_SELECTOR,".js_parent_party_name").click()
        self.driver.find_element(By.CSS_SELECTOR,".ww_dialog_body .jstree-anchor").click()
        self.driver.find_element(By.CSS_SELECTOR,".ww_dialog_foot .ww_btn_Blue").click()

