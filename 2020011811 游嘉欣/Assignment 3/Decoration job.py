"""
    Author：Jacy
    Purpose：Pass
    Created:2022/6/17
"""
import math
import random
from functools import wraps
#flag can be ACC or MCC
def decorateWith(flag):
    def decorator(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = TN = FP = FN = 0
            for e in result:
                if (e[0] is True) and (e[1] is True):
                    TP += 1
                elif (e[0] is True) and (e[1] is False):
                    FN += 1
                elif (e[0] is False) and (e[1] is True):
                    FP += 1
                elif (e[0] is False) and (e[1] is False):
                    TN += 1
                else:
                    pass
            if flag == "ACC":
                Acc = (TP + TN) / total
                print("ACC : %f" % Acc)
            elif flag == "MCC":
                Mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC : %f" % Mcc)
            else:
                pass
            return result
        return wrapper
    return decorator

# @Decorator
@decorateWith("MCC")
@decorateWith("ACC")
def generateRandom(**kargs):
    result = list()
    num = kargs["num"]
    struct = kargs["struct"]
    for i in range(num):
        elem = list()
        for key, value in struct.items():
            if key == "int":
                it = iter(value["range"])
                elem.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(value["range"])
                elem.append(random.uniform(next(it), next(it)))
            elif key =="str":
                Range = value["range"]
                Length = value["length"]
                string = ""
                for j in range(Length):
                    string+=random.choice(Range)
                elem.append(string)
            elif key == "bool":
                for k in range(value["num"]):
                    elem.append(random.choice((True, False)))
            else:
                elem.append("未知类型")
        result.append(elem)
    return result

argument = {"num":10000, "struct":{"bool":{"num":2}}}
resultList = generateRandom(**argument)
