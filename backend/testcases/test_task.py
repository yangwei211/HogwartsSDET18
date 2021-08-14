# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/8/12 9:47 上午
@file: test_task.py
@desc: 
"""
import requests


class TestTask:
    """
    测试人物的接口测试用例
    """

    def setup_class(self):
        self.base_url = "http://localhost:5000/task"

    def test_get_task(self):
        r = requests.get(self.base_url)
        assert r.status_code == 200

    def test_post_task(self):
        """
        新增测试任务的测试用例
        :return:
        """
        # 用例的信息
        data = {"nodeid": "test_setup_teardown.py"}
        r = requests.post(self.base_url, json=data)
        assert r.status_code==200