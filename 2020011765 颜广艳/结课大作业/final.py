import random
import math
from functools import wraps

# yield 生成器
class Random:
    def __init__(self, **kwargs):
        self.__num = kwargs["num"]
        self.__struct = kwargs["struct"]

    def __iter__(self):
        for i in range(self.__num):
            if i == self.__num:
                raise StopIteration
            element = list()
            for key, val in self.__struct.items():
                if key == "int":
                    it = iter(val["datarange"])
                    element.append(random.randint(next(it), next(it)))
                elif key == "float":
                    it = iter(val["datarange"])
                    element.append(random.uniform(next(it), next(it)))
                elif key =="str":
                    element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
                elif key == "bool":
                    for j in range(val["datarange"]):
                        element.append(random.choice((True, False)))
                else:
                    element.append(" ")
            yield element


#flag 可以是 ACC 或者 MCC
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

@decorateWith("MCC")
@decorateWith("ACC")
def getRandoms(**kwargs):
    generator = Random(**kwargs)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList

data = {"num":5,"struct":{"bool":{"datarange":2}}}

resultList = getRandoms(**data)

for item in resultList:
    print(item)