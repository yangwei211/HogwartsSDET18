# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/23 11:10 上午
@file: digui.py
@desc: 
"""
import json


def recursion(data):
    """
    :param data: 原始数据
    :return: 在原始数据基础上，修改float类型，对float类型做数据翻倍操作
    """
    if isinstance(data, dict):
        # 如果是字典类型，继续递归value值
        for k, v in data.items():
            data[k] = recursion(v)

    elif isinstance(data, list):
        # data_new = []
        # for i in data:
        #     data_new.append(recursion(i))
        data = [recursion(i) for i in data]

    elif isinstance(data, float):
        data = data * 2

    else:
        data = data

    return data


if __name__ == '__main__':
    test_data = json.load(open("quote.json", encoding="UTF-8"))
    print(json.dumps(recursion(test_data)))
