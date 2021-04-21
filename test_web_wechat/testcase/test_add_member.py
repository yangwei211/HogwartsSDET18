# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/18 2:53 下午
@file: test_add_member.py
@desc: 
"""
import pytest

from test_web_wechat.page.add_member import AddMemberPage
from test_web_wechat.page.main_page import MainPage


class TestAddMember:
    """
    编写测试用例
    """

    def setup_class(self):
        self.main_page = MainPage()

    # 实现测试数据有页面对象分离
    @pytest.mark.parametrize(("username,accid,phone"), [("皮城女警", "0090", "16619836638")])
    def test_add_member(self, username, accid, phone):
        # 1.跳转到添加成员页面        2，添加成员                    3.获取成员列表
        name_list = self.main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
        assert username in name_list

    @pytest.mark.parametrize(("username,accid,phone"), [("皮城女警", "0090", "13426207522")])
    def test_add_member_fail(self, username, accid, phone):
        data_list = self.main_page.goto_add_member().add_member_fail(username, accid, phone)
        err = [i for i in data_list if i != ""]
        assert "皮城女警" in err[0]


    def test_xxx(self):
        main_page = MainPage()
        main_page.goto_add_member().add_xxx().add_member()
