# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/8/10 10:34 下午
@file: testcases.py
@desc: 
"""
# 类代表是哪个接口资源，每个方法代表对此资源的操作，比如get/post
# 在类服务中继承resouce,表示使用flask-restful
from flask import request
from flask_restful import Resource

from backend.models.testcases import Testcase
from backend.server import app, db


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
        return {"error": 0, "msg": {"data": data}}

    def post(self):
        # 增加一条用例
        case_data = request.json
        app.logger.info(case_data)
        # 从接口中拿到的字典数据进行解包，使用关键字传参传入Testcase
        testcase = Testcase(**case_data)
        # 如果数据字段存在列表，需要做一次转换
        # 每次如果dumps，那么字符串会添加""
        # testcase.nodeid = json.dumps(request.json.get('nodeid'))
        db.session.add(testcase)
        db.session.commit()
        return {"error": 0, "message": "post success"}

    def put(self):
        # 修改
        # 获取被修改的接口信息
        case_id = request.json.get("id")
        # 通过id找到被修改的接口信息然后做修改操作
        case = Testcase.query.filter_by(id=case_id). \
            update(request.json)
        # 修改之后commit到数据库
        db.session.commit()
        app.logger.info(f'数据已修改，id{case}被修改为{request.json}')
        return {"error": 0, "msg": {"id": case}}

    def delete(self):
        case_id = request.args.get('id')
        if not case_id:
            return {'error': 40001, "msg": "delete case_id can't be null"}
        # 返回一个主键
        case = Testcase.query.filter_by(id=case_id).delete()
        db.session.commit()
        app.logger.info(case)

        return {"error": 0, "msg": {"id": case}}