# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/4/10 3:19 下午
@file: test_add.py
@desc: 
"""
import allure
import pytest
import yaml
from Calculator import Calculator

def get_datas():
    with open('./data/calc.yaml') as f:
        datas = yaml.safe_load(f)
        # print(data)
    return datas

@pytest.fixture(params=get_datas()['int_datas'],ids=get_datas()['ids'])
def get_datas_calc(request):
    return request.param

def test_get_datas(get_datas_calc):
    print(get_datas_calc)

@allure.feature("计算器")
class TestCal:
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # def teardown_class(self):
    #     print("计算结束")

    # @pytest.mark.parametrize('a,b,expect', get_datas()['int_datas'], ids=get_datas()['ids'])
    @allure.story("相加-整数")
    def test_add_int(self,initcalc_class, get_datas_calc):
        assert get_datas_calc[2] == initcalc_class.add(get_datas_calc[0], get_datas_calc[1])

    @pytest.mark.parametrize('a,b,expect',[ [0.1,0.1,0.2],[0.1,0.2,0.3]
                             ],ids=['浮点数','浮点数2'])
    @allure.story("相加-浮点数")
    def test_add_float(self,initcalc_class,a,b,expect):
        assert expect == round(initcalc_class.add(a,b),2)

    @pytest.mark.parametrize('a,b,expect',[ [0.1,0,False],[2,2,2]])
    @allure.story("相除")
    def test_div(self,initcalc_class,a,b,expect):
        try:
            assert expect == initcalc_class.div(a,b)
        except ZeroDivisionError:
            print("除数为0")