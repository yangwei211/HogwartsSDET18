

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):

        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # caps['platformVersion']='6.0'
        caps["deviceName"] = "hogwarts"
        caps["settings[waitForIdleTimeout]"]=0
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        # self.driver.update_settings({'waitForIdleTimeout':0})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    def test_addcontact(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='必填']").send_keys("测试123")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='必填']").send_keys("13111111111")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']")