import random
import string

'''
平时作业一：编写一个函数，生成给定个数的数据结构的随机数据，
要求使用关键字参数给定数据结构，并从外部文本文件中读取相应数据结构的字典作为关键字参数传入函数
'''


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
    open_file = open("data.txt")
    para = eval(open_file.read())
    result = structDataSampling(**para)
    for item in result:
        print(item)

apply()