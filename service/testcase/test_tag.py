# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/23 1:40 下午
@file: test_weweork.py
@desc: 
"""
from jsonpath import jsonpath

from service.api.tag.tag import Tag
from service.api.wework_api import WeWork


class TestTag:

    # def setup_class(self):
    #     self.tag = Tag()
    #     self.tag.get_token()
    #
    # def teardown_class(self):
    #     # 如果进程被临时终止，teardown*方法可能得不到执行，所以为了稳定，尽量不要在teardown*中放入重要的逻辑
    #     pass

    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        self.tag.clear()
        #todo: 追加测试数据

    def teardown_class(self):
        # 如果进程被临时终止，teardown*方法可能得不到执行，所以为了稳定法，尽量不要在teardown中放入重要的逻辑
        pass

    def test_search(self):
        r = self.tag.search()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        assert len(r.json()['tag_group'])==0

    def test_add(self):
        # 新增标签
        # todo: 数据唯一性，1.提前清理数据（推荐）2.使用时间戳代表唯一性

        # data={
        #     'group_name': "tag_group_052301",
        #     'tag_list': [
        #         {
        #             "name": "tag_052301"
        #         }
        #     ]
        # }
        # r = self.tag.add(data)
        tag_list = [{'name': "tag_052301"},{'name': "tag_052302"}]
        r = self.tag.add(tag_list=tag_list, group_name="tag_group_052301")

        assert r.json()['errcode'] == 0

        # done：代码冗余
        r = self.tag.search()
        assert r.json()['errcode'] == 0
        assert 'tag_group_052301' in [group['group_name'] for group in r.json()['tag_group']]

        # 使用jsonpath
        tag_name_list=jsonpath(r.json(),'$..tag[*].name')
        print(tag_name_list)
        assert set(['tag_052301','tag_052302']) == set(tag_name_list)

    def test_order(self):
        # 新增标签
        # todo: 数据唯一性，1.提前清理数据（推荐）2.使用时间戳代表唯一性

        # 明确需求，排序是后端负责还是前段负责
        tag_list = [
            {'name': "tag_0523011",'order':2},
            {'name': "tag_0523012",'order':1},
            {'name': "tag_0523013",'order':3}
        ]
        r = self.tag.add(tag_list=tag_list, group_name="tag_group_052302")

        assert r.json()['errcode'] == 0

        # done：代码冗余
        r = self.tag.search()
        assert r.json()['errcode'] == 0
        assert 'tag_group_052302' in [group['group_name'] for group in r.json()['tag_group']]

        # 使用jsonpath
        tag_name_list=jsonpath(r.json(),'$..tag[*].name')
        print(tag_name_list)
        # 前段工程师负责排序，所以不验证排序
        # assert ['tag_0523012','tag_0523011','tag_0523013'] == tag_name_list
        # 验证数据值就可以了


    def test_delete(self):
        # 删除数据与添加数据尽量区分开，失败的时候可以更好的直观看到feature失败
        # todo 判断新增内容是的在search结果中
        r = self.tag.delete("xxxxx")
        assert r.json()['errcode'] == 0
        r = self.tag.search()
        # TODO 业务逻辑验证 判断删除的内容是否已经消失在search结果中
