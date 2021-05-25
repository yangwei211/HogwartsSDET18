# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/24 10:20 下午
@file: base_api.py
@desc: 
"""
import json

import requests


class BaseApi:
    def request(self, request: dict):
        # 为了多协议支持，或者将来协议变更，或者将来方便切换不同的http库，比如requests切换到其他的lib
        if "url" in request:
            return self.http_request(request)
        if 'rpc' == request.get("protocol"):
            return self.rpc_request(request)

    def http_request(self, request):
        r = requests.request(**request)
        #todo: 后面换成logging
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self):
        pass

    def tcp_request(self):
        pass


