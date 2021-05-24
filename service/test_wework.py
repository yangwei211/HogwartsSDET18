# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/23 1:40 下午
@file: test_weweork.py
@desc: 
"""
import json

import requests


class TestWeWork:

    # def setup_class(self):
    #     self.tag = Tag()
    #     self.tag.get_token()
    #
    # def teardown_class(self):
    #     # 如果进程被临时终止，teardown*方法可能得不到执行，所以为了稳定，尽量不要在teardown*中放入重要的逻辑
    #     pass

    def setup_class(self):
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

    # def test_token(self):
    #     r = requests.get(
    #         "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #         params={
    #             "corpid":"ww847e782df3f260fa",
    #             "corpsecret":"LYvo6ZjWgs91xEFLXAjeYapnQ1vp3Spw3m0LuMwlZrY"
    #         }
    #     )
    #     print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    #     # print(r.json())
    #     assert r.status_code == 200
    #     print(r.json()['access_token'])

    def test_search(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token},
            json={}
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_tag(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token": self.token},
            json={
                "group_name":"tag_group_0523001",
                "tag":[
                    {
                        "name":"tag_0523001",
                    }
                ]
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()['errcode'] == 200
        assert r.json()['errcode'] == 0

    def test_tag_delete_(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={
                "tag_id": "etoM0gDAAAxrgNGHdUANswZAB6Anb5Bg"
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.json()['errcode'] == 0