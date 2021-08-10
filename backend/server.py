# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/7/13 3:03 下午
@file: server.py
@desc: 
"""
import json

from flask import Flask, request
from flask_restful import Resource, Api
# 实例化flask对象
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
# 解决跨域
CORS(app, supports_credentials=True)
# 使用MySQL进行连接
username = 'root'
pwd = 'admin'
ip = '192.168.31.94'
port = '3306'
database = 'test_ck18'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 解决数据库warning问题
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)


def router():
    """
    路由管理
    """
    from backend.apis.testcases import TestCaseService
    api.add_resource(TestCaseService, "/testcase")


if __name__ == '__main__':
    # 把服务添加到app flask中
    # 第一个参数是添加的接口服务，第二个参数，是指定对应接口服务使用的路由
    # db.create_all()

    app.run(debug=True)
