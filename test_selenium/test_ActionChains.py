# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/18 12:13 下午
@file: test_ActionChains.py
@desc: 
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH,'//input[@value="click me"]')
        element_dpubleclick = self.driver.find_element(By.XPATH,'//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element(By.XPATH,'//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_dpubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)





