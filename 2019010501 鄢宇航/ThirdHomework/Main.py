# 实现2个修饰器ACC和MCC，对模拟二分类预测结果的精度和马修相关系数进行计算，其中模拟预测结果采用随机数生成函数作为被修饰函数


# 带参数修饰器通用写法
import math
from functools import wraps
#
#
# def addLogging(decPara):  # 修饰器的参数
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("%s is running" % func.__name__)
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator


# @ACC 精度相关统计
# @MCC 马修相关系数统计

import random


def ACC(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        right = 0
        print("%s is running" % func.__name__)
        exa = func(*args, **kwargs)
        for i in range(10000):
            if exa[i][0] == exa[i][1]:
                right = right + 1
        print("ACC is %f" % (int(right) / 10000))
        return exa

    return wrapper


def MCC(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        fn = tp = fp = tn = 0
        print("%s is running" % func.__name__)
        exa = func(*args, **kwargs)
        for i in range(10000):
            if exa[i][0] == exa[i][1] == bool(1):
                tp = tp + 1
            if exa[i][0] == exa[i][1] == bool(0):
                tn = tn + 1
            if exa[i][0] != exa[i][1] == bool(1):
                fp = fp + 1
            if exa[i][0] == exa[i][1] == bool(0):
                fn = fn + 1

        print("MCC is %f" % ((tp * tn - fp * fn) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))))
        return exa

    return wrapper


@ACC
def pred1(struct):
    # 随机数生成两列一万行 布尔值:结果/预测

    for i in range(10000):
        ele = []
        res = random.choice([True, False])
        pre = random.choice([True, False])
        ele.append(res)
        ele.append(pre)
        struct.append(ele)
    return struct


example = []

pred1(example)


@MCC
def pred2(struct):
    # 随机数生成两列一万行 布尔值:结果/预测

    for i in range(10000):
        ele = []
        res = random.choice([True, False])
        pre = random.choice([True, False])
        ele.append(res)
        ele.append(pre)
        struct.append(ele)
    return struct


example = []
pred2(example)
