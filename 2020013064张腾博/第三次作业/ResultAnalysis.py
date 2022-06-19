"""
    Author: 2020013064张腾博
    Purpose: Assignment3
    Created: 2022.6.19
"""
import random
from math import sqrt
from functools import wraps


class _ResultAnalysis:
    """
    DESCRIPTION:
    A decorator
    To analysis the result of function
    with popular methods such as ACC, MCC
    其中
    TP：被检索到正样本，实际也是正样本（正确识别）
    FP：被检索到正样本，实际是负样本（一类错误识别）
    FN：未被检索到正样本，实际是正样本。（二类错误识别）
    TN：未被检索到正样本，实际也是负样本。（正确识别）
    Accuracy:
    ACC = (TP + TN) / (TP + TN + FP + FN)
    Matthews correlation coefficient:
    MCC = (TP * TN - FP * FN) / ((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) ^ 1/2
    """
    def __init__(self, func, method="ACC"):
        self.__func = func
        self.__method = method

    def __call__(self, *args, **kwargs):
        try:
            results = self.__func(*args, **kwargs)
        except ValueError:
            print("ValueError")
            return None
        if self.__method == "ACC":
            return self.ACC(results)
        elif self.__method == "MCC":
            return self.MCC(results)

    def ACC(self, data):
        TP = TN = FP = FN = 0
        for i in data:
            if i[0] & i[1]:
                TP += 1
            elif i[0] & ~i[1]:
                TN += 1
            elif ~i[0] & i[1]:
                FP += 1
            elif ~i[0] & ~i[1]:
                FN += 1
        res = (TP + TN) / (TP + TN + FP + FN)
        return res

    def MCC(self, data):
        TP = TN = FP = FN = 0
        for i in data:
            if i[0] & i[1]:
                TP += 1
            elif i[0] & ~i[1]:
                TN += 1
            elif ~i[0] & i[1]:
                FP += 1
            elif ~i[0] & ~i[1]:
                FN += 1
        res = (TP * TN - FP * FN) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        return res


def ResultAnalysis(func, method):
    # 没错，看似是类修饰器，实则是函数修饰器，要不然我也不知道咋传参
    @wraps(func)
    def wrapper(function):
        return _ResultAnalysis(function, method)
    return wrapper


@ResultAnalysis("ACC", "ACC")
def structDataSampling(num, struct):
    """
    :param num:
    :param struct:
    :return:
    """
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in struct.items():
            if key is int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key is float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key is str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key is bool:
                for _ in range(0, value['times']-1):
                    tmp = random.choice([True, False])
                    element.append(tmp)
                tmp = random.choice([True, False])
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def apply1():
    struct = {bool: {"times": 2}}
    result = structDataSampling(10000, struct)
    print("The is the result of ACC:")
    print(result)


apply1()


@ResultAnalysis("MCC", "MCC")
def structDataSampling(num, struct):
    """
    :param num:
    :param struct:
    :return:
    """
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in struct.items():
            if key is int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key is float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key is str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key is bool:
                for _ in range(0, value['times']-1):
                    tmp = random.choice([True, False])
                    element.append(tmp)
                tmp = random.choice([True, False])
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def apply2():
    struct = {bool: {"times": 2}}
    result = structDataSampling(10000, struct)
    print("The is the result of MCC:")
    print(result)


apply2()
