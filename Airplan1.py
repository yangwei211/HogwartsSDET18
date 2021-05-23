# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/6 10:46 下午
@file: Airplan1.py
@desc: 
"""


class Airplan:
    # name
    name = ""
    # color
    color = ""

    def set_color(self, color):
        self.color = color
        print(f"飞机的颜色是:{self.color}")

    def set_name(self, name):
        self.name = name
        print(f"飞机的名字是:{self.name}")


# 民用机
class CivilAirplan(Airplan):
    zhongliang = ""

    def load_person(self, num):
        print(f"民用机能载人的数量为:{num}")

    def set_name(self, name):
        print("民用机的set_name")


# 军用机
class JunyAirplan(Airplan):
    name = "军用机"

    def set_name(self, name1):
        print(f"当前{self.name} 的名字为: {name1}")


civilAirplan = CivilAirplan()
civilAirplan.set_color("民用机的颜色：红色")
civilAirplan.load_person(11)
civilAirplan.set_name("民用机1号")
print(civilAirplan.zhongliang)

junyair = JunyAirplan()
junyair.set_name("军用机1号")

# air1 = Airplan()
# air1.set_name("第一架飞机")
# air1.set_color("红色")
#
# air2 = Airplan()
# air2.set_name("第二架飞机")
# air2.set_color("绿色")
