"""
    @Author  : Ruiyan Li
    @File    : homework1.py
    @Software: PyCharm
    @Describe: 编写一个函数，生成给定个数的数据结构的随机数据，要求使用关键字参数给定数据结构，并从外部文本文件中读取相应数据结构的字典作为关键字参数传入函数
"""

import random
import string


def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def txtFileReader(file):
    fr = open(file, 'r', encoding="utf-8")
    content = fr.read()
    return eval(content)


def apply():
    res = structDataSampling(**txtFileReader('liry.txt'))
    for i in iter(res):
        print(i)
        
        
apply()
