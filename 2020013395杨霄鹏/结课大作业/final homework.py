import math
import random
from functools import wraps

def ACC(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        TP = 0
        FP = 0
        result = func(*args, **kwargs)
        for index in range(0,args[0]):
            i = next(result)
            if i[0] == 1 and i[1] == 1:
                TP = TP + 1
            elif i[0] == 1 and i[1] == 0:
                FP = FP + 1
        acc = TP / (TP + FP)
        return acc
    return wrapper


@ACC
def structDataSampling(num, **kwargs):
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "int2":
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
        yield element


dic = {"int": {"datarange": (0, 1)},"int2": {"datarange": (0, 1)}}
acc = structDataSampling(10000, **dic)
print(acc)

def MCC(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for index in range(0, args[0]):
            i = next(result)
            if i[0] == 1 and i[1] == 1:
                TP = TP + 1
            elif i[0] == 1 and i[1] == 0:
                FP = FP + 1
            elif i[0] == 0 and i[1] == 1:
                TN = TN + 1
            elif i[0] == 0 and i[1] == 0:
                FN = FN + 1
        N = TN + TP + FN + FP
        S = (TP + FN) / N
        P = (TP + FP) / N
        mcc = (TP / N - S * P) / math.sqrt(P * S * (1 - S) * (1 - P))
        return mcc
    return wrapper


@MCC
def structDataSampling(num, **kwargs):
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "int2":
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
        yield element


dic = {"int": {"datarange": (0, 1)},"int2": {"datarange": (0, 1)}}
mcc = structDataSampling(10000, **dic)
print(mcc)