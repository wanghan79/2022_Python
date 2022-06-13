# -*- coding: UTF-8 -*-
"""
author:Binghe Luo
date:2022/6/3 9:50
"""
from math import sqrt
import random


def ResultAnalysis(flag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            all = len(result)
            TP = 0
            TN = 0
            FP = 0
            FN = 0
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
                acc = (TP + TN) / all
                print("ACC : %f" % acc)
            elif flag == "MCC":
                mcc = (TP * TN - FP * FN) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC : %f" % mcc)
            else:
                pass
            return result
        return wrapper
    return decorator


@ResultAnalysis("MCC")
@ResultAnalysis("ACC")
def function(**kwargs):
    result = list()
    num = kwargs["num"]
    struct = kwargs["struct"]
    for i in range(num):
        element = list()
        for key, val in struct.items():
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
                break
        result.append(element)
    return result
argument = {"num": 10000, "struct": {"bool": {"num": 2}}}
resultList = function(**argument)



