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
CORS(app,supports_credentials=True)
# 使用MySQL进行连接
username='root'
pwd='admin'
ip='192.168.31.94'
port='3306'
database='test_ck18'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 解决数据库warning问题
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)


class Testcase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        """
        返回一个标准的Python结构体
        :return:
        """
        return {'id':self.id, 'nodeid':self.nodeid,'remark':self.remark}

# 类代表是哪个接口资源，每个方法代表对此资源的操作，比如get/post
# 在类服务中继承resouce,表示使用flask-restful
class TestCaseService(Resource):
    """
    测试用例服务
    """
    # 方法名，对应app.route中的methods
    def get(self):
        """
        查询接口，查询用例数据信息
        """
        # request 获取 接口发过来的请求信息
        # 查询单条数据信息
        case_id = request.args.get("id")
        if case_id:
            # 当传入caseID时，查询单条数据信息
            case_data = Testcase.query.filter_by(id=case_id).first()
            app.logger.info(case_data)
            # data = [{"id":case_data.id, "nodeid":case_data.nodeid, "remark":case_data.remark}]
            data = [case_data.as_dict()]
        else:
            # 反之查询所有的用例信息
            case_data = Testcase().query.all()
            # app.logger.info(case_data)
            # data =[{"id":i.id, "nodeid":i.nodeid, "remark":i.remark} for i in case_data]
            data = [i.as_dict() for i in case_data]
            # app.logger.info(data)
        return {"error":0,"msg":{"data":data}}

    def post(self):
        # 增加一条用例
        case_data = request.json
        app.logger.info(case_data)
        # 从接口中拿到的字典数据进行解包，使用关键字传参传入Testcase
        testcase = Testcase(**case_data)
        # 如果数据字段存在列表，需要做一次转换
        testcase.nodeid = json.dumps(request.json.get('nodeid'))
        db.session.add(testcase)
        db.session.commit()
        return {"error":0,"message":"post success"}

    def put(self):
        # 修改
        # 获取被修改的接口信息
        case_id = request.json.get("id")
        # 通过id找到被修改的接口信息然后做修改操作
        case = Testcase.query.filter_by(id=case_id).\
            update(request.json)
        db.session.commit()
        app.logger.info(f'数据已修改，id{case}被修改为{request.json}')
        return {"error":0,"msg":{"id": case}}

    def delete(self):
        case_id = request.args.get('id')
        if not case_id:
            return {'error':40001,"msg":"delete case_id can't be null"}
        # 返回一个主键
        case = Testcase.query.filter_by(id=case_id).delete()
        db.session.commit()
        app.logger.info(case)

        return {"error":0,"msg":{"id": case}}




if __name__ == '__main__':
    # 把服务添加到app flask中
    # 第一个参数是添加的接口服务，第二个参数，是指定对应接口服务使用的路由
    # db.create_all()
    api.add_resource(TestCaseService,"/testcase")
    app.run(debug=True)