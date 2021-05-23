# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/7 10:57 下午
@file: test_标准库time.py
@desc: 
"""
import time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
#
# print(time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()))


# 获取两天前的时间

now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2

time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))





