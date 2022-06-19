# @Time        : 2022/6/17 13:11
# @Author      : 2020012968 肖开宇
# @File        : decorator.py
# @Description : 第三次平时作业

import random
from math import sqrt

"""
ACC=(TP+TN)/(TP+FP+FN+TN)
MCC=(TP*TN-FP*FN)/(sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN)))
TP（True Positive）： 预测结果为正类，实际上就是正类
FP（False Positive）：预测结果为正类，实际上却是反类
FN（False negative）：预测结果为反类，实际上却是正类
TN（True negative）： 预测结果为反类，实际上就是反类
"""


# ACC：Accuracy指标
def ACC(func):
    def wrap(*args, **kwargs):
        count = 0
        data = func(*args, **kwargs)
        total = len(data)
        for i in range(total):
            if data[i][0] == data[i][1]:
                count += 1
        acc = count / total
        print("ACC = %f" % acc)
        return data

    return wrap


# MCC：马修相关系数
def MCC(func):
    def wrap(*args, **kwargs):
        data = func(*args, **kwargs)
        TP, FP, TN, FN = 0, 0, 0, 0
        for i in data:
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
    samples = []
    for i in range(0, keys['num']):
        sample = []
        for key, value in keys['struct'].items():
            if key == "int":
                daterange = iter(value['datarange'])
                sample.append(random.randint(next(daterange), next(daterange)))
            elif key == "float":
                daterange = iter(value['datarange'])
                sample.append(random.uniform(next(daterange), next(daterange)))
            elif key == "str":
                sample.append(''.join(random.choice(value['datarange']) for _ in range(value['len'])))
            elif key == "bool":
                for ith in range(value["num"]):
                    sample.append(random.choice((True, False)))
            else:
                break
        samples.append(sample)
    return samples


para = {'num': 1000, 'struct': {'bool': {"num": 2}}}
getRandomData(**para)
