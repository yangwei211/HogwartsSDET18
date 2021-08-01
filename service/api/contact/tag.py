# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/29 6:59 下午
@file: tag.py
@desc: 
"""
from service.api.wework_api import WeWork


class Tag(WeWork):
    def add(self,name):
        data={

        }
        return self.request(data)

    def search(self):
        pass

    def uptdate(self):
        pass

    def delete(self):
        pass