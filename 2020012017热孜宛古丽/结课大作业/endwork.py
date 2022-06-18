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
            total = len(result)  #total是Accuracy中正确的预测结果的数量
            tp = tn = fp = fn = 0
            for item in result:
                if (item[0] is True)&(item[1] is True):
                    tp=tp+1  #预测对，预测结果为正
                elif (item[0] is True)&(item[1] is False):
                    fn= fn+1  #预测错，预测结果为负
                elif (item[0] is False)&(item[1] is True):
                    fp=fp+1   #预测错，预测结果为正
                elif (item[0] is False) & (item[1] is False):
                    tn=tn+1   #预测对，预测结果为负
                else:
                    pass
            if flag == "ACC":
                acc = (tp + tn) / total
                print("ACC : %f" % acc)
            elif flag == "MCC":
                t = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
                if(t == 0):
                    t = 1
                mcc = (tp * tn - fp * fn) / t
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


argument = {"num":5,"struct":{"bool":{"num":2}}}
resultList = getRandoms(**argument)

# for elem in resultList:
#     print(elem)


