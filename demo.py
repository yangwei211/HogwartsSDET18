# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/13 10:16 下午
@file: demo.py
@desc: 
"""
from flask import Flask, session, request, Request, make_response

app = Flask(__name__)
request: Request
app.secret_key = 'key'


@app.route("/request", methods=['GET', 'POST'])
def hello():
    query = request.args
    post = request.form
    return f"query: {query}\n" \
           f"post: {post}"


@app.route("/session")
def session_handler():
    for k, v in request.args.items():
        session[k] = v
    resp = make_response({k: v for k, v in session.items()})
    for k, v in request.args.items():
        resp.set_cookie(f"cookie_{k}", v)
    return resp
