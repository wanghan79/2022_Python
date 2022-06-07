import random
from functools import wraps
import math

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

    def structDataSampling(self):
        result = list()
        for i in range(self.num):
            element = list()
            for key,value in self.struct.items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it),next(it))
                    element.append(tmp)
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it),next(it))
                    element.append(tmp)
                elif key == "bool":
                    for ith in range(value["datarange"]):
                        element.append(random.choice((1, 0)))
                elif key == "str":
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(0,value['len']) )
                    element.append(tmp)
                else :
                    break
            result.append(element)
        return result

argument = {"num":10000,"struct":{"bool":{"datarange":2}}}

@decorateWith("ACC")
@decorateWith("MCC")
def getRandoms():
    random = Random(**argument)
    result = random.structDataSampling()
    return result

getRandoms()


