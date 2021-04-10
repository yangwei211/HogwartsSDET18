# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/10 5:08 下午
@file: test_div.py
@desc: 
"""
import pytest

from Calculator import Calculator


class TestCal:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect',[
        [1,1,1],[10,2,5],[100,4,25],[0,1,0]
    ],ids=['int1', 'float','bignum','zeronum'])
    def test_div(self,a,b,expect):
        assert expect == self.calc.div(a,b)
        print(self.calc.div(a,b))