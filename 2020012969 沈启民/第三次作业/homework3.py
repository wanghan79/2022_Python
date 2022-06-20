import math
import random
from functools import wraps


def ACC_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args,**kwargs)
        TP = TN = FP = FN = 0
        for x in data:
            if (x[0] is True) and (x[1] is True):
                TP += 1
            elif (x[0] is False) and (x[1] is False):
                TN += 1
            elif (x[0] is False) and (x[1] is True):
                FP += 1
            elif (x[0] is True) and (x[1] is False):
                FN += 1
            else:
                pass
        acc = (TP + TN) / len(data)
        print("ACC值为：%f" % acc)
        return data
    return wrapper

def MCC_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args,**kwargs)
        TP = TN = FP = FN = 0
        for x in data:
            if (x[0] is True) and (x[1] is True):
                TP += 1
            elif (x[0] is False) and (x[1] is False):
                TN += 1
            elif (x[0] is False) and (x[1] is True):
                FP += 1
            elif (x[0] is True) and (x[1] is False):
                FN += 1
            else:
                pass
        mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC值为：%f" % mcc)
        return data
    return wrapper

para = {"num": 10000, "struct": {"bool": {"range": 2}}}

@MCC_decorator
@ACC_decorator
def Random_Bool(*args, **kwargs):
    result = list()
    for index in range(0,kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "bool":
                for i in range(value["range"]):
                    element.append(random.choice((True, False)))
            else:
                break
        result.append(element)
    return result


Random_Bool(**para)
# print(Random_Bool(**para))

