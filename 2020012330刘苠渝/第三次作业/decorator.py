import random
from functools import wraps
import math


def ACC(func):
    wraps(func)

    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        TP = TN = FP = FN = 0
        for e in data:
            if (e[0] == 1) and (e[1] == 1):
                TP += 1
            elif (e[0] == 0) and (e[1] == 0):
                TN += 1
            elif (e[0] == 0) and (e[1] == 1):
                FP += 1
            elif (e[0] == 1) and (e[1] == 0):
                FN += 1
            else:
                pass
        acc = (TP + TN) / len(data)
        print("ACC：%f" % acc)
        return data

    return wrapper


def MCC(func):
    wraps(func)

    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        TP = TN = FP = FN = 0
        for e in data:
            if (e[0] == 1) and (e[1] == 1):
                TP += 1
            elif (e[0] == 0) and (e[1] == 0):
                TN += 1
            elif (e[0] == 0) and (e[1] == 1):
                FP += 1
            elif (e[0] == 1) and (e[1] == 0):
                FN += 1
            else:
                pass
        mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC：%f" % mcc)
        return data

    return wrapper


@ACC
@MCC
def GetRandomData(**kwargs):
    result = list()
    for i in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == "str":
                element.append(''.join(random.choice(value['datarange']) for i in range(value['len'])))
            elif key == "bool":
                for ith in range(value["num"]):
                    element.append(random.choice((True, False)))
            else:
                break
        result.append(element)
    return result


argument = {'num': 1000, 'struct': {'bool': {"num": 2}}}
GetRandomData(**argument)
