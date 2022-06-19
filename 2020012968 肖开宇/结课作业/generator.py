# @Time        : 2022/6/18 13:55
# @Author      : 2020012968 肖开宇
# @File        : generator.py
# @Description : 结课作业

import random
from math import sqrt


# ACC：Accuracy指标
def ACC(func):
    def wrap(*args, **kwargs):
        count, total = 0, 0
        data = []
        for i in func(*args, **kwargs):
            data.append(i)
            if i[0] == i[1]:
                count += 1
            total += 1
        acc = count / total
        print("ACC = %f" % acc)
        return data

    return wrap


# MCC：马修相关系数
def MCC(func):
    def wrap(*args, **kwargs):
        data = []
        TP, FP, TN, FN = 0, 0, 0, 0
        for i in func(*args, **kwargs):
            data.append(i)
            if i[0] & i[1]:
                TP += 1
            elif i[0] & (~i[1]):
                FP += 1
            elif ~i[0] & ~i[1]:
                TN += 1
            elif ~i[0] & i[1]:
                FN += 1
        mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC = %f" % mcc)
        return data

    return wrap


@MCC
@ACC
def getRandomData(**keys):
    for i in range(0, keys['num']):
        for key, value in keys['struct'].items():
            if key == "int":
                daterange = iter(value['datarange'])
                yield random.randint(next(daterange), next(daterange))
            elif key == "float":
                daterange = iter(value['datarange'])
                yield random.uniform(next(daterange), next(daterange))
            elif key == "str":
                yield ''.join(random.choice(value['datarange']) for _ in range(value['len']))
            elif key == "bool":
                yield [random.choice((True, False)) for _ in range(value["num"])]
            else:
                break


para = {'num': 10000, 'struct': {'bool': {"num": 2}}}
getRandomData(**para)
