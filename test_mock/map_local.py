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
from mitmproxy import http


class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        # 匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
                in flow.request.url and "SZ00" in flow.request.url:
                with open("quote.json", encoding="UTF-8") as f:
                    flow.response = http.HTTPResponse.make(
                        # 状态码
                        200,
                        # 响应体, 传入的数据格式是String
                        f.read(),
                        # 响应头
                    )

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # if 条件代表匹配规则
        pass


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
    # mitmdump()
