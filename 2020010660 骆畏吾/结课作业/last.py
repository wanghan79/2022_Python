"""
Author:weiw
Purpose:pass.
Created:6/16
"""
import math
import random
from functools import wraps

class Random:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for i in range(self.num):
            if i == self.num:
                raise StopIteration
            element = list()
            for key, value in self.struct.items():
                if key == "int":
                    it = iter(value["range"])
                    element.append(random.randint(next(it), next(it)))
                elif key == "float":
                    it = iter(value["range"])
                    element.append(random.uniform(next(it), next(it)))
                elif key == "str":
                    strRange = value["range"]
                    strLength = value["length"]
                    string = ""
                    for j in range(strLength):
                        string += random.choice(strRange)
                    element.append(string)
                elif key == "bool":
                    for ith in range(value["num"]):
                        element.append(random.choice((True, False)))
                else:
                    element.append("未知类型")
            yield element

def re_decorate(flag):
    def decorator(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = 0
            TN = 0
            FP = 0
            FN = 0
            for re in result:
                if (re[0] is True) and (re[1] is True):
                    TP += 1
                elif (re[0] is True) and (re[1] is False):
                    FN += 1
                elif (re[0] is False) and (re[1] is True):
                    FP += 1
                elif (re[0] is False) and (re[1] is False):
                    TN += 1
                else:
                    pass
            if flag == "ACC":
                acc = (TP + TN) / total
                print("ACC : %f" % acc)
            elif flag == "MCC":
                denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                mcc = (TP * TN - FP * FN) / denominator
                print("MCC : %f" % mcc)
            else:
                pass
            return result
        return wrapper
    return decorator

@re_decorate("MCC")
@re_decorate("ACC")
def getRandom(**kwargs):
    gen = Random(**kwargs)
    resultList = []
    for element in gen:
        resultList.append(element)
    return resultList

argument = {"num":5,"struct":{"bool":{"num":2}}}

resultList = getRandom(**argument)

for elem in resultList:
    print(elem)