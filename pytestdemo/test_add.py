# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/10 3:19 下午
@file: test_add.py
@desc: 
"""
import pytest
import yaml
from Calculator import Calculator


class TestCal:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    def getdatas(self):
        with open('./data/calc.yaml') as f:
            datas = yaml.safe_load(f)
            # print(data)
        return datas

    @pytest.mark.parametrize('a,b,expect', [
        getdatas()['int_datas'],
    ], ids=getdatas()['ids'])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)
