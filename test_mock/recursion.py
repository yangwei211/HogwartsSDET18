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

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # if 条件代表匹配规则
        # 匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
            in flow.request.url and "SZ00" in flow.request.url:
            base_data = json.loads(flow.response.text)
            new_data = self.recursion(base_data, 0)
            flow.response.text = json.dumps(new_data)

    def recursion(self, data, int_data = 1):
        """
        :param data: 原始数据
        :return: 在原始数据基础上，修改float类型，对float类型做数据翻倍操作
        """
        if isinstance(data, dict):
            # 如果是字典类型，继续递归value值
            for k, v in data.items():
                data[k] = self.recursion(v, int_data)

        elif isinstance(data, list):
            # data_new = []
            # for i in data:
            #     data_new.append(recursion(i))
            data = [self.recursion(i, int_data) for i in data]

        elif isinstance(data, float):
            data = data * int_data

        else:
            data = data

        return data



addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
    # mitmdump()
