"""
Author:weiw
Purpose:pass.
Created:6/15
"""
import random
import math
from functools import wraps

#ACC or MCC
def re_decorate(flag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = 0
            TN = 0
            FP = 0
            FN = 0
            for re in result:
                if (re[0] is True) and (re[1] is True):
                    TP += 1
                elif (re[0] is True) and (re[1] is False):
                    FN += 1
                elif (re[0] is False) and (re[1] is True):
                    FP += 1
                elif (re[0] is False) and (re[1] is False):
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

@re_decorate("MCC")
@re_decorate("ACC")

def getRandom(**kwargs):
    result = list()
    num = kwargs["num"]
    struct = kwargs["struct"]
    for index in range(num):
        element = list()
        for key, val in struct.items():
            if key == "bool":
                for ith in range(val["num"]):
                    element.append(random.choice((True, False)))
            else:
                element.append("未知类型")
        result.append(element)
    return result


argument = {"num": 10000, "struct": {"bool": {"num": 2}}}

resultList = getRandom(**argument)
