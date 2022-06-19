""" 
    @Time    : 2022/6/10 10:25
    @Author  : Jiaxuan Jiang
    @Email   : 6812624@qq.com
    @File    : homework1.py
    @Software: PyCharm
"""
import string
import random


def structDataSampling(**kwargs):
    """
    :Description: Generate random data for a given number of data structures
    :param kwargs:
    :return:
    """
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['dataRange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['dataRange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                it = iter(value['dataRange'])
                tmp = ''.join(random.SystemRandom().choice(value['dataRange']) for _ in range(8))
            elif key == "bool":
                tmp = []
                for i in range(value['cnt']):
                    tmp.append(random.choice((True, False)))
                tmp = tuple(tmp)
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def callFunc():
    text = open("struct.txt")
    index = 0
    while True:
        line = text.readline()  # 按行读取
        if not line:  # 读到文件尾停止
            break
        index += 1
        print("Group {}".format(index))
        struct = eval(line)
        result = structDataSampling(**struct)
        for element in result:
            print(element)


callFunc()
