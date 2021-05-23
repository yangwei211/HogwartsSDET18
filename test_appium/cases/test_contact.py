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
from test_appium.utils.contact_info import ContactInfo


class TestContact:


    def setup_class(self):
        self.contactinfo=ContactInfo()
        self.app = App()

    def setup(self):
        # 启动
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        name = self.contactinfo.get_name()
        phonenum = self.contactinfo.get_phonenum()
        self.main.goto_contactList().goto_addmember().\
            addmember_bymenual().edit_member(name,phonenum).find_tost()

    def test_addcontact1(self):
        name = self.faker.name()
        phonenum = self.faker.phone_number()
        self.main.goto_contactList().goto_addmember(). \
            addmember_bymenual().edit_member(name,phonenum).find_tost()

    def test_deletecontact(self):
        self.main.goto_contactList().goto_contactinfo().delete_contact()











