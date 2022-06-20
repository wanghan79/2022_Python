import random
import math
from math import sqrt
from functools import wraps
import string
def ACC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):
        data = list(fuc(*args, **kwargs))
        print(f"randomDate = {data}")
        num=len(data)
        count = 0
        for i in range(num):
            if data[i][0] == data[i][1]:
                count += 1
        print(f"ACC = {count / num}")
        return data
    return wrap

def MCC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):
        data = list(fuc(*args, **kwargs))
        tp, fp, tn, fn = 0, 0, 0, 0
        for item in data:
            if item[0] & item[1]:
                tp += 1
            elif item[0] & (~item[1]):
                fp += 1
            elif ~item[0] & ~item[1]:
                tn += 1
            elif ~item[0] & item[1]:
                fn += 1
        numerator = (tp * tn) - (fp * fn)
        denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        MCC = numerator / denominator
        print(f"MCC = {MCC}")
        return data
    return wrap
@MCC
@ACC

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


def getRandoms(**kwargs):
    generator = Random(**kwargs)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList

Result = {"num": 1000,
        "struct": {"bool": {"num" : 2}}
          }

AnswerList = getRandoms(**Result)

for item in AnswerList:
    print(item)
