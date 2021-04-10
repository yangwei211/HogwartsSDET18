# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/10 3:19 下午
@file: test_add.py
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
        [1,1,2],[0.1,0.1,0.2],[1000,1000,2000],[0,1000,1000]
    ],ids=['int1', 'float','bignum','zeronum'])
    def test_add(self,a,b,expect):
        assert expect == self.calc.add(a,b)

