# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/6/8 10:21 下午
@file: test_div1.py
@desc: 
"""
import pytest

@pytest.fixture(params=[[0.1,0,False],[2,2,2],[10,1,10]],ids=['zero','int','int1'])
def get_div_datas(request):
    return request.param

def test_get_div_datas(get_div_datas):
    print(get_div_datas)

#参数化功能，用fixture实现
class TestDiv:
    # @pytest.mark.parametrize('a,b,expect',[ [0.1,0,False],[2,2,2]])
    def test_div(self,initcalc_class,get_div_datas):
        try:
            assert get_div_datas[2] == initcalc_class.div(get_div_datas[0],get_div_datas[1])
        except ZeroDivisionError:
            print("除数为0")