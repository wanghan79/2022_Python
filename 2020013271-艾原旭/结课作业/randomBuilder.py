import math
import random
from functools import wraps

def decorateWith(flag):
    def decorator(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = TN = FP = FN = 0
            for e in result:
                if (e[0] == 1) and (e[1] == 1):
                    TP += 1
                elif (e[0] == 1) and (e[1] == 0):
                    FN += 1
                elif (e[0] == 0) and (e[1] == 1):
                    FP += 1
                elif (e[0] == 0) and (e[1] == 0):
                    TN += 1
                else:
                    pass
            if flag == "ACC":
                acc = (TP + TN) / total
                print("ACC : %f" % acc)
            elif flag == "MCC":
                denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                if(denominator == 0):
                    denominator = 1
                mcc = (TP * TN - FP * FN) / denominator
                print("MCC : %f" % mcc)
            else:
                pass
            return result
        return wrapper
    return decorator

class Random:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for i in range(self.num):
            element = list()
            for key,value in self.struct.items():
                if key == "bool":
                    for ith in range(value["datarange"]):
                        element.append(random.choice((1, 0)))
                else :
                    break
            yield element

argument = {"num":10000,"struct":{"bool":{"datarange":2}}}

@decorateWith("ACC")
@decorateWith("MCC")
def getRandoms():
    generator = Random(**argument)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList
getRandoms()