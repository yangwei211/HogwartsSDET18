# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/8/10 10:36 下午
@file: task.py
@desc: 
"""
from flask import request
from flask_restful import Resource

from backend.models.task import Task
from backend.server import app, db
from backend.utils.execute_tools import ExecuteTools


class TaskService(Resource):
    def post(self):
        """
        1.调用jenkins执行用例
        2.执行用例之后，写入执行记录到数据库表中
        :return:
        """
        # 具体执行的用例从post请求的信息，请求体中获取
        data = request.json
        nodeid = data.get('nodeid')
        # 调用jenkins执行测试用例
        report = ExecuteTools.invoke(nodeid)
        app.logger.info(f"添加一条task，报告为{report},执行用例为{nodeid}")
        # 没有传主键，因为主键会自动生成，所以不传递也可以
        # 没有传创建时间，因为创建时间有默认时间
        # 对task数据库做写入操作
        task = Task(remark=nodeid, report=report)
        db.session.add(task)
        db.session.commit()
        db.session.close()
        return {"error": 0, "msg": "ok"}

    def get(self):
        """

        :return:
        """
        # 查询task所有的数据
        tasks = Task.query.all()
        # as_dict把对象转成python字典格式，后面falks好解析
        tasks_data = [task.as_dict() for task in tasks]
        app.logger.info(f"获取到的任务列表为{tasks_data}")
        return {"error": 0, "msg": {"data": tasks_data}}
