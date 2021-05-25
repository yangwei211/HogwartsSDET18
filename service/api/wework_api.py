# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/23 2:27 下午
@file: wework_api.py
@desc: 
"""
import json

import requests

from service.api.base_api import BaseApi


class WeWork(BaseApi):
    # 可以不用加的，只是为了声明类型，Python也开始支持类型了，是Python3的一个技巧
    token = None

    def get_token(self):
        # r = requests.get(
        #     "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     params={
        #         "corpid": "ww847e782df3f260fa",
        #         "corpsecret": "LYvo6ZjWgs91xEFLXAjeYapnQ1vp3Spw3m0LuMwlZrY"
        #     }
        # )

        # 具体的api对象通过这样的设计，可以实现数据化，为以后的自动生成奠定一个好的基础
        data = {
            "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            'method': 'get',
            "params":{
                "corpid": "ww847e782df3f260fa",
                "corpsecret": "LYvo6ZjWgs91xEFLXAjeYapnQ1vp3Spw3m0LuMwlZrY"
        }
        }
        r = self.request(data)

        assert r.status_code == 200
        self.token = r.json()['access_token']
