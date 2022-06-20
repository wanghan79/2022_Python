"""
    @Author  : Ruiyan Li
    @FIle    : homework1.py
    @Software: PyCharm
    @Describe: 编写一个函数，生成给定个数的数据结构的随机数据，要求使用关键字参数给定数据结构，并从外部文本文件中读取相应数据结构的字典作为关键字参数传入函数
"""

import random
import string


def structDataSampling(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
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
    dic = {}
    for line in fr:
        list = line.strip().split(' ') # 读取每行的数据，以空格为分界符
        if list[0] == 'str':
            dic[list[0]] = {list[1]: list[2], list[3]: int(list[4])}
            # {‘str' : {'datarange' : 'ABCDEFGIJKLNOSADSIHCOZ' , 'len': 100 }}

        else:
            dic[list[0]] = {list[1]: [int(list[2]), int(list[3])]}
            # {'float' : {'datarange' : [-100, 100] }}

    return dic




def apply():

    res = structDataSampling(100, **txtFileReader('liry.txt'))
    for i in iter(res):
        print(i)

apply()
