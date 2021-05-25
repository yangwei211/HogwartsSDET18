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

from service.api.wework_api import WeWork


class Tag(WeWork):

    def search(self):
        data={
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "method": 'post',
            "params":{"access_token": self.token},
            "json":{}
        }
        return self.request(data)

    def add(self, tag_name, group_name):
        data={
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "method": 'post',
            "params":{"access_token":self.token},
            "json":{
                "group_name":group_name,
                "tag":[
                    {
                        "name":tag_name,
                    }
                ]
        }

        }
        return self.request(data)

    def delete(self, tag_id):
        data={
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "method": 'post',
            "params":{"access_token": self.token},
            "json":{
                "tag_id": tag_id
            }
        }
        return self.request(data)
