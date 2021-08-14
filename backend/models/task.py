# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/8/10 10:34 下午
@file: testcases.py
@desc:
"""
import datetime

from backend.server import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 人物执行的相关数据信息
    remark = db.Column(db.String(120))
    report = db.Column(db.String(120))
    # 指定时间格式，默认值为当前时间
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def as_dict(self):
        """
        返回一个标准的Python结构体
        :return:
        """
        return {'id': self.id,
                'remark': self.remark,
                'report': self.report,
                # 强转为字符串的格式
                'create_at': str(self.create_at)
                }


if __name__ == '__main__':
    db.create_all()
