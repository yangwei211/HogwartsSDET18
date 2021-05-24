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


class WeWork:
    token = None

    def get_token(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={
                "corpid": "ww847e782df3f260fa",
                "corpsecret": "LYvo6ZjWgs91xEFLXAjeYapnQ1vp3Spw3m0LuMwlZrY"
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200
        self.token = r.json()['access_token']

    def search(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token},
            json={}
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def add(self, tag_name, group_name):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token": self.token},
            json={
                "group_name":group_name,
                "tag":[
                    {
                        "name":tag_name,
                    }
                ]
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def delete(self, tag_id):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={
                "tag_id": tag_id
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r