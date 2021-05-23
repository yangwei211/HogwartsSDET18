# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2021/5/6 11:23 下午
@file: test_标准库.py
@desc: 
"""
import os


# os.mkdir("testdir")
# print(os.listdir("./"))
# os.removedirs("testdir")
# print(os.getcwd())


print(os.path.exists("b"))
if not  os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt","w")
    f.write("hello ,os using")
    f.close()