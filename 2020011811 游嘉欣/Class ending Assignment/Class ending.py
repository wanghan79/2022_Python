"""
    Author：Jacy
    Purpose：Pass
    Created:2022/6/17
"""
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
            elem = list()
            for key, value in self.struct.items():
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
            yield elem


#flag can be ACC or MCC
def decorateWith(flag):
    def decorator(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = TN = FP = FN = 0
            for ele in result:
                if (ele[0] is True) and (ele[1] is True):
                    TP += 1
                elif (ele[0] is True) and (ele[1] is False):
                    FN += 1
                elif (ele[0] is False) and (ele[1] is True):
                    FP += 1
                elif (ele[0] is False) and (ele[1] is False):
                    TN += 1
                else:
                    pass
            if flag == "ACC":
                Acc = (TP + TN) / total
                print("ACC : %f" % Acc)
            elif flag == "MCC":
                denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                if(denominator == 0):
                    denominator = 1
                Mcc = (TP * TN - FP * FN) / denominator
                print("MCC : %f" % Mcc)
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

argument = {"num":1000,"struct":{"bool":{"num":2}}}

resultList = getRandoms(**argument)
