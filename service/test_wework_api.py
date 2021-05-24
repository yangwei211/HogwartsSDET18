# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/23 1:40 下午
@file: test_weweork.py
@desc: 
"""

from service.wework_api import WeWork


class TestWeWork:

    # def setup_class(self):
    #     self.tag = Tag()
    #     self.tag.get_token()
    #
    # def teardown_class(self):
    #     # 如果进程被临时终止，teardown*方法可能得不到执行，所以为了稳定，尽量不要在teardown*中放入重要的逻辑
    #     pass

    def setup_class(self):
        self.wework = WeWork()
        self.wework.get_token()

    def test_search(self):
        r = self.wework.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag(self):
        # 新增变迁
        # todo: 数据唯一性，1.提前清理数据（推荐）2.使用时间戳代表唯一性
        r = self.wework.add(tag_name="tag_052301",group_name="tag_group_052301")
        assert r.json()['errcode'] == 0

        # todo：代码冗余
        r = self.wework.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag_delete_(self):
        r = self.wework.delete("xxxxx")
        assert r.json()['errcode'] == 0
        r = self.wework.search()
        # TODO 业务逻辑验证
