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
                MCC = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC : %f" % MCC)
            else:
                pass
            return result
        return wrapper
    return decorator



# @Decorator
@decorateWith("MCC")
@decorateWith("ACC")
def GetRandomData(**kwargs):
    result = list()
    for i in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == "str":
                element.append(''.join(random.choice(value['datarange']) for i in range(value['len'])))
            elif key == "bool":
                for ith in range(value["num"]):
                    element.append(random.choice((True, False)))
            else:
                break
        result.append(element)
    return result


argument = {'num': 1000, 'struct': {'bool': {"num": 2}}}
GetRandomData(**argument)
