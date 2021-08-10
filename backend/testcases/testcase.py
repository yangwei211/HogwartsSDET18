# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/7/13 11:10 上午
@file: test_case.py
@desc: 
"""
# 测试用例
# 被测对象：自己编写的接口
# 测试代码：对自己编写的接口的测试
import requests


class TestCase:
    """
    测试用例接口模块的测试代码
    """

    def setup_class(self):
        self.base_url = "http://127.0.0.1:5000/testcase"

    def test_get(self):
        """
        测试获取用例数据
        :return:
        """
        r = requests.get(self.base_url, params={"id": 1})
        print(r.json())
        assert r.status_code == 200

    def test_post(self):
        """
        测试新增用例
        :return:
        """
        # 添加用例数据
        # data = {"id": 1, "nodeid":"node111", "remark":"备注1"}
        # data2 = {"id": 2, "nodeid":"node02", "remark":"备注22222"}
        data2 = {"nodeid": "xxxxx", "remark": "备注3"}

        r = requests.post(self.base_url, json=data2)
        # 测试数据库
        assert r.status_code == 200

    def test_put(self):
        """
        测试修改用例
        :return:
        """
        data2 = {"id": 2, "nodeid": "node02", "remark": "第二次修改"}
        r = requests.put(self.base_url, json=data2)
        print(r.json())
        assert r.status_code == 200

    def test_delete(self):
        """
        测试删除用例
        :return:
        """

        # r = requests.delete(self.base_url)
        # print(r.json())
        # assert r.json()['error'] == 40001
        # assert r.status_code == 200
        r = requests.delete(self.base_url, params={'id': 3})
        print(r.json())
        assert r.status_code == 200
