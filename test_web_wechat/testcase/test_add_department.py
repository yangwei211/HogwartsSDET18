# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/21 10:47 下午
@file: test_add_department.py
@desc: 
"""
from test_web_wechat.page.main_page import MainPage
class TestAddDepartment:

    def setup_class(self):
        self.main_page = MainPage()

    # @pytest.mark.parametrize(("departname"), [("测试部门")])
    def test_add_department_fail(self):
        self.main_page.goto_contact().goto_add_department().add_department()