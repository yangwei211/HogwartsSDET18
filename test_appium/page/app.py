# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/24 4:22 下午
@file: app.py
@desc: 
"""

# app相关的操作：启动，关闭，重启
from appium import webdriver

from test_appium.page.main_page import MainPage


class App:

    def start(self):

        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["settings[waitForIdleTimeout]" ] =0
        # caps['dontStopAppOnReset']= True
        caps["noReset"] = "true"
        caps["skipDeviceInitialization" ]= True
        # caps["skipServerInstallation"]=True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        return self


    def restart(self):
        pass

    def stop(self):
        pass

    def goto_main(self):
        # 入口
        return MainPage(self.driver)