# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/16 4:27 下午
@file: rewrite.py
@desc: 
"""
import http

"""HTTP-specific events."""
import mitmproxy.http
import json


class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        # 匹配规则

            # with open("quote.json",encoding="utf-8") as f:
            #     flow.response = http.HTTPResponse.make(
            #     200,
            #     f.read()
            # )

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # if 条件代表匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
                in flow.request.url and "SZ00" in flow.request.url:
            # 数据的模拟
            data = json.loads(flow.response.text)
            # 修改股票名称数据
            data['data']['items'][0]['quote']['name'] = "hogwarts1"
            data['data']['items'][1]['quote']['name'] = "hogwarts2"
            data['data']['items'][2]['quote']['name'] = "hogwarts3"
            # 修改股票涨跌幅
            data['data']['items'][0]['quote']['percent'] = "0.01"
            data['data']['items'][1]['quote']['percent'] = "-0.01"
            data['data']['items'][2]['quote']['percent'] = "0"
            # 修改响应
            print(data)
            flow.response.text = json.dumps(data)

addons = [
    Events()
]


if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
    # mitmdump()
