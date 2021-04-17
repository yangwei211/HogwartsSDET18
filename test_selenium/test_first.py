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


class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()
        # self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 - 主页")
        ele = self.driver.find_element_by_link_text("霍格沃兹测试学院 – 软件自动化测试开发培训_接口性能测试")
        assert ele

class TestWework:
    def test_Wework(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("menu_contacts").click()
        print(self.driver.get_cookies())
        cookie = self.driver.get_cookies()
        with open("data.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)

def test_cookie():
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850473645871'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'I-bAl9s-rxEfCzyrOSTEHizvmg67fzxOxR-Gj2Ml8GMiIQ5cwSCum6E9IN9lp8ijn1FyC73RT2L365Ml7ECxMEhkuzRhmhEW9kKOYjKdkVB8AcVOh9CeAl9X71yeKFkjWe_x4nUdzOol5NLDIjZlKs8UIh1YDvpZpDgabp78CRLVRHgJpDzOmPiNxGQyJ-9r210un9io5jC-F1l-GqVOhtV2OjqmWdbi8ff2Tb0C4z9ePk9QiaotMI59pvYc_SsDfAld_QK-Sjk9nAYqm7I02w'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850473645871'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325040450976'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'ruaOFLRxZsgJK-4c9jc3jx8SDDZ_tOeE4XAfx_CAcWSzedRqRd136M1VGrtXlcjK'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9101901'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650195253, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618658098,1618659014,1618659119,1618659254'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618659254'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '21840058552053545'}, {'domain': '.qq.com', 'expiry': 1618745665, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1542225202.1618647843'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618679253, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'vdn067'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 1618659314, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1681731265, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1013319468.1618647843'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650183717, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621251297, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(3)

def test_cookie_v2():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("data.yaml",encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()


    sleep(3)























