import random
from functools import wraps
import math


# Type:either ACC Or MCC
def decorateWith(Type):
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
            if Type == "ACC":
                acc = (TP + TN) / total
                print("ACC : {}".format(acc))
            elif Type == "MCC":
                temp = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                mcc = (TP * TN - FP * FN) / temp
                print("MCC : {}".format(mcc))
            else:
                pass
            return result

        return wrapper

    return decorator


#yield
class structDataSampling:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for i in range(self.num):
            element = list()
            for key, value in self.struct.items():
                if key == "bool":
                    number = value['num']
                    for i in range(0, number):
                        tmp = random.choice((True, False))
                        element.append(tmp)
                else:
                    break
            yield element


argument = {"num": 10, "struct": {"bool": {"num": 4}}}
@decorateWith("MCC")
@decorateWith("ACC")
def getResult():
    generator = structDataSampling(**argument)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList
for item in getResult():
    print(item)


