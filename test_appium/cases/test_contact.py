# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/24 4:23 下午
@file: test_contact.py
@desc: 
"""
from faker import Faker

from test_appium.page.app import App


class TestContact:
    def setup_class(self):

        self.faker = Faker('zh-CN')

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name = self.faker.name()
        phonenum = self.faker.phone_number()
        self.main.goto_contactList().goto_addmember().\
            addmember_bymenual().edit_member(name,phonenum).find_tost()