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


def get_datas():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    return datas


def test_getdatas():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    print(datas)


class TestCal:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',
        get_datas()['int_datas']
    , ids=get_datas()['ids'])
    def test_add_int(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3],
    ], ids=['float1', 'float2'])
    def test_add_int_float(self, a, b, expect):
        assert expect == round(self.calc.add(a, b), 2)

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0, False], [2, 2, 2]])
    def test_div(self, a, b, expect):
        try:
            assert expect == self.calc.div(a, b)
        except ZeroDivisionError:
            print("除数为0")
