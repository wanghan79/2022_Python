# @Time        : 2022/6/15 11:54
# @Author      : 2020012968 肖开宇
# @File        : main.py
# @Description : 第一次平时作业


import random
import string


# 生成给定个数的数据结构的随机数据
def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


# 从外部文本文件中读取相应数据结构的字典
def apply():
    txt_file = open("para.txt")
    para = eval(txt_file.read())
    result = structDataSampling(**para)
    for item in result:
        print(item)


apply()
