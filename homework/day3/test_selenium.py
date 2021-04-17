# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/17 3:56 下午
@file: test_first.py
@desc: 
"""
from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWework:
    def test_Wework(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("menu_contacts").click()
        cookie = self.driver.get_cookies()
        with open("data.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)



def test_cookie_v2():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("data.yaml",encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    driver.find_element_by_link_text("添加成员").click()
    driver.implicitly_wait(5)
    driver.find_element_by_id("username").click()
    driver.find_element_by_id("username").send_keys("test")
    driver.find_element_by_id("memberAdd_acctid").send_keys("test")
    driver.find_element_by_id("memberAdd_phone").send_keys("16618836638")
    driver.find_element_by_link_text("保存").click()
    sleep(3)























