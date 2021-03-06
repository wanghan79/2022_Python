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

def ACC(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        TP, TN, FP, FN = 0, 0, 0, 0
        for e in data:
            if e[0] == 1:
                TP = TP + 1 if e[1] == 1 else TP
                FP = FP + 1 if e[1] == 0 else FP
            else:
                FN = FN + 1 if e[1] == 1 else FN
                TN = TN + 1 if e[1] == 0 else TN
        acc = (TP + TN) / len(data)
        print("ACC ： %f" % acc)
        return data

    return wrapper

def MCC(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        TP, TN, FP, FN = 0, 0, 0, 0
        for e in data:
            if e[0] == 1:
                TP = TP + 1 if e[1] == 1 else TP
                FP = FP + 1 if e[1] == 0 else FP
            else:
                FN = FN + 1 if e[1] == 1 else FN
                TN = TN + 1 if e[1] == 0 else TN
        mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC ： %f" % mcc)
        return data

    return wrapper


@ACC
@MCC
def getRandomNum(**kwargs):
    generator = Random(**kwargs)
    result = []
    for item in generator:
        result.append(item)
    return result

data = {"num": 10000, "struct": {"bool": {"range": 2}}}

getRandomNum(**data)
