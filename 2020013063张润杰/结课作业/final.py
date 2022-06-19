import random
from functools import wraps
import math
class Random:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]
    def __iter__(self):
        for i in range(self.num):
            if i == self.num:
                raise StopIteration
            element = list()
            for key, val in self.struct.items():
                if key == "int":
                    it = iter(val["range"])
                    element.append(random.randint(next(it), next(it)))
                elif key == "float":
                    it = iter(val["range"])
                    element.append(random.uniform(next(it), next(it)))
                elif key =="str":
                    strRange = val["range"]
                    strLength = val["length"]
                    string = ""
                    for j in range(strLength):
                        string+=random.choice(strRange)
                    element.append(string)
                elif key == "bool":
                    for ith in range(val["num"]):
                        element.append(random.choice((True, False)))
                else:
                    element.append("未知类型")
            yield element
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
                ACC = (TP + TN) / total
                print("ACC : %f" % ACC)
            elif flag == "MCC":
                denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                if(denominator == 0):
                    denominator = 1
                MCC = (TP * TN - FP * FN) / denominator
                print("MCC : %f" % MCC)
            else:
                pass
            return result
        return wrapper
    return decorator
@decorateWith("MCC")
@decorateWith("ACC")
def getRandoms(**kwargs):
    generator = Random(**kwargs)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList
argument = {"num":10000,"struct":{"bool":{"num":2}}}
resultList = getRandoms(**argument)