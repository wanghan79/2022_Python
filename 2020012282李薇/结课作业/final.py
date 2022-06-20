"""
    Author: liwei
    Purpose: pass.
"""
"""
    Author: liwei
    Purpose: pass.
"""
import string
import random
import math
from functools import wraps

class ResultAnalysis:
    def __init__(self, func,static="ACC"):
        self.__func = func
        self.__static = static

    def __call__(self, *args, **kwargs):
        result = self.__func(*args, **kwargs)
        if result is None:
            return None
        if self.__static == "ACC":
            return self.ACC(result)
        elif self.__static == "MCC":
            return self.MCC(result)

    def ACC(self, data):
        def wrap(*args, **kwargs):
            count = 0
            data = fun(*args, **kwargs)
            n = len(data)
            for i in range(n):
                if data[i][0] == data[i][1]:
                    count += 1
            acc = count / n
            print("ACC = {}".format(acc))
            return data
        return wrap

    def MCC(self, data):
        def wrap(*args, **kwargs):
            data = fun(*args, **kwargs)
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
            print("MCC = {}".format(mcc))
            return data
        return wrap

para = {"num": 1000, "struct": {"int": {"datarange": (0, 100)}, "float": {"datarange": (0, 10000)},"str": {"datarange": string.ascii_uppercase, "len": 50}}}

def Resultanalysis(static):
    def wrapper(func):
        return ResultAnalysis(func, static)
    return wrapper

@Resultanalysis("ACC")
def structDataSamplingACC(num, **kwargs):
    for item in range(0, num):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                it = iter(value['datarange'])
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(8))
            else:
                break
        yield element.append(tmp)

acc = structDataSamplingACC(**para)
print(acc)


@Resultanalysis("MCC")
def structDataSamplingMCC(num, **kwargs):
    for item in range(0, num):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                it = iter(value['datarange'])
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(8))
            else:
                break
        yield element.append(tmp)

mcc = structDataSamplingMCC(**para)
print(mcc)

