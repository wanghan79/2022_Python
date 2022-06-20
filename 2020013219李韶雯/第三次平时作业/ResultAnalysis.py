"""
Author: LSW
"""
import math
import random


def calculating(flag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
           # print(result)
            s = len(result)
            TP = TN = FP = FN = 0
            for i in result:
                if(i[0] is True) and (i[1] is True):
                    TP += 1
                elif(i[0] is True) and (i[1] is False):
                    FN += 1
                elif (i[0] is False) and (i[1] is True):
                    FP += 1
                elif (i[0] is False) and (i[1] is False):
                    TN += 1
                else:
                    pass
            if flag == "ACC":
                acc = (TP + TN) / s
                print("ACC : %f" % acc)
            elif flag == "MCC":
                mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC : %f" % mcc)
            else:
                pass
            return result
        return wrapper
    return decorator


@calculating("MCC")
@calculating("ACC")
def structDataSampling(**kwargs):
    """

    :param kwargs: 字典类型的结构体
    :return: 随机生成的结构
    """
    result = list()
    for index in range(0,kwargs["num"]):
        element = list()
        for key,value in kwargs["struct"].items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it),next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it),next(it)))
            elif key == "str":
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            elif key == "bool":
                for i in range(value['datarange']):
                    element.append(random.choice((True,False)))
            else:
                break
        result.append(element)
    return result


struct = {"num": 10000, "struct": {"bool": {"datarange": 2}}}
structDataSampling(**struct)

