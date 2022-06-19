#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


def get_data(num, **kwargs):
    result = []
    for index in range(0, num):
        element = []
        for key, value in kwargs.items():
            if key in "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key in "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key in 'str':
                tmp = ''
                for i in range(0, value['len']):
                    tmp = tmp + random.SystemRandom().choice(value['datarange'])
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def read_text(filePath_1):
    with open(filePath_1, 'r') as f:
        _list = f.readlines()
    _list = [x.strip('\n') for x in _list]
    rtnLst = [('struct=' + n) for n in _list]
    return rtnLst


struct = {}


def main():
    filePath_1 = input('输入文件路径: ')
    rand_time = int(input('输入随机采样时间: '))
    getLst = read_text(filePath_1)
    for n in getLst:
        exec(n, globals())  # Monkey Patch (Hotfix)
        randomResult = get_data(rand_time, **struct)
        for item in randomResult:
            print(item)

main()