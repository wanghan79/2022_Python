#coding=utf-8
import math
import random
from functools import wraps

class Random:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for i in range(self.num):
            element = list()
            for key, val in self.struct.items():
                if key == "int":
                    it = iter(val["range"])
                    element.append(random.randint(next(it), next(it)))
                elif key == "float":
                    it = iter(val["range"])
                    element.append(random.uniform(next(it), next(it)))
                elif key == "str":
                    element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
                elif key == "bool":
                    for i in range(val["range"]):
                        element.append(random.choice((True, False)))
                else:
                    break
            yield element

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
        acc = (TP + TN) / (TP + TN + FP + FN)
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

@MCC_decorator
@ACC_decorator
def getRandoms(**kwargs):
    generator = Random(**kwargs)
    result = []
    for item in generator:
        result.append(item)
    return result

# para1 = {"num":5,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(0,10000)},"str":{"datarange":string.ascii_uppercase,"len":50}}}
para = {"num": 10000, "struct": {"bool": {"range": 2}}}

getRandoms(**para)
# print(getRandoms(**para))