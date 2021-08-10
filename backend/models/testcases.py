# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/8/10 10:34 下午
@file: testcases.py
@desc: 
"""
from backend.server import db


class Testcase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        """
        返回一个标准的Python结构体
        :return:
        """
        return {'id': self.id, 'nodeid': self.nodeid, 'remark': self.remark}

