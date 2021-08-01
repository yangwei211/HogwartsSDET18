# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/7/13 8:49 上午
@file: demo.py
@desc: 
"""
# 路由定义
# 设定请求方法
# 获取请求参数
# 获取请求体
# 不要看成requests!!!!!!
from flask import Flask, request
# 实例化flask对象
app = Flask(__name__)

# 指定路由，每一次，访问此路由，都会执行方法里的内容
# 通过method参数设置访问方法
@app.route("/",methods=['get','post'])
# @app.route("/",methods=['get'])
def hello_world():
    # request.args获取请求url中的参数信息
    id = request.args.get("id")
    # return str(id)
    # request.json获取请求体中的数据信息
    return request.json

    # return "<p>Hello, World!</p>"

@app.route("/hogwarts")
def hello_hogwarts():
    return "<p>Hello, hogwarts1111222222!</p>"


if __name__ == '__main__':
    # 直接调用app.run 方法，启用后端服务
    # 通过port参数指定端口
    # debug=True 的时候是热加载,方便调试后端逻辑
    app.run(debug=True,port=8000)