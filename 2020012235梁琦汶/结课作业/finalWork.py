"""
 Author:CreamCheese
 purpose:pass
 created:2022/6/20 00:05
"""
import random
from functools import wraps
import math


class Random:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for item in range(self.num):
            if item == self.num:
                raise StopIteration
            element = list()
            for key, value in self.struct.items():
                if key == "int":
                    it = iter(value["datarange"])
                    element.append(random.randint(next(it), next(it)))
                elif key == "float":
                    it = iter(value["datarange"])
                    element.append(random.uniform(next(it), next(it)))
                elif key == "str":
                    strRange = value["datarange"]
                    strLength = value["length"]
                    string = ""
                    for j in range(strLength):
                        string += random.choice(strRange)
                    element.append(string)
                elif key == "bool":
                    for i in range(value["num"]):
                        element.append(random.choice((True, False)))
                else:
                    break
            yield element


#  flag can be ACC or MCC
def addLogging(flag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = TN = FP = FN = 0
            for e in result:
                if (e[0] is True) and (e[1] is True):
                    TP += 1
                elif (e[0] is True) and (e[1] is False):
                    TN += 1
                elif (e[0] is False) and (e[1] is True):
                    FP += 1
                elif (e[0] is False) and (e[1] is False):
                    FN += 1
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


@addLogging("MCC")
@addLogging("ACC")
def getRandomData(**kwargs):
    generator = Random(**kwargs)
    result = []
    for element in generator:
        result.append(element)
    return result


def main():
    struct = {'num': 10000, 'struct': {'bool': {"num": 2}}}
    format(getRandomData(**struct))


if __name__ == '__main__':

    main()