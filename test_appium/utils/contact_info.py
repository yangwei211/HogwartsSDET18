# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/29 11:19 下午
@file: contact_info.py
@desc: 
"""
from faker import Faker


class ContactInfo:
    def __init__(self):
        self.faker = Faker('zh-CN')

    def get_name(self):
        name = self.faker.name()
        return name

    def get_phonenum(self):
        phonenum = self.faker.phone_number()
        return phonenum


if __name__ == '__main__':
    contact_info = ContactInfo()
    print(contact_info.get_name())
    print(contact_info.get_phonenum())