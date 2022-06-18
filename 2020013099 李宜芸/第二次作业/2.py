#coding:utf-8

import my_package
import yaml


def read_func(path):
    with open(path, 'r') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)[0]
        func_name = value["func_name"]
        args = list(map(int, value["args"].split(" ")))
        func = getattr(my_package, func_name)
        if func:
            res = func(*args)
            return res
        else:
            print("包中没有该函数！")

path = './read.yml'

print(read_func(path))