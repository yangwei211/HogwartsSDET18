# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/23 1:40 下午
@file: test_weweork.py
@desc: 
"""
from time import sleep

from jsonpath import jsonpath

from service.api.externalcontact.tag import Tag
from service.api.wework_api import WeWork
from service.testcase.base_testcase import BaseTestcase


class TestTag(BaseTestcase):


    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()
        self.tag.clear()
        #todo: 追加测试数据
        self.prepare_testdata()

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
        r = self.tag.add(tag_list=tag_list,group_name="tag_group_052302")

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
        # 准备数据的两个方案 1、添加（不要复用上一步的用例。独立添加，除非添加是个很重的工作 2.setup中添加一批可用数据

        # todo 判断新增内容是的在search结果中

        self.tag.add([{'name':"tag_052901"}],group_name='tag_group_052911')
        sleep(2)
        # 不需要再调用search方法验证add结果
        r = self.tag.delete(['tag_052901'])
        print("11111")
        print(r)
        # assert r.json()['errcode'] == 0
        r = self.tag.search()
        print("222222")
        print(r)
        # assert 'tag_group_052911' not in [group['group_name'] for group in r.json()['tag_group']]
        # TODO 业务逻辑验证 判断删除的内容是否已经消失在search结果中

    def test_flow(self):
        # 冒烟测试
        # 线上巡检测试
        # 重要测试数据
        # 全流程测试用例 添加 修改 删除 查询
        pass