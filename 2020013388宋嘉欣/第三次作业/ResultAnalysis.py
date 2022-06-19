import math
import random
from functools import wraps

#ACC准确率 MCC马修系数
def decorate(flag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            TP = TN = FP = FN = 0
            for x in result:
                if (x[0] is True) and (x[1] is True):
                    TP += 1
                elif (x[0] is True) and (x[1] is False):
                    FN += 1
                elif (x[0] is False) and (x[1] is True):
                    FP += 1
                elif (x[0] is False) and (x[1] is False):
                    TN += 1
                else:
                    pass
            if flag == "ACC":
                acc = (TP + TN) / len(result)
                print("ACC: %f" % acc)
            elif flag == "MCC":
                mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC: %f" % mcc)
            else:
                pass
            return result

        return wrapper

    return decorator


@decorate("MCC")
@decorate("ACC")
def RandomData(**kwargs):
    result = list()
    num = kwargs["num"]
    struct = kwargs["struct"]
    for i in range(num):
        element = list()
        for key, val in struct.items():
            if key == "bool":
                for ith in range(val["num"]):
                    element.append(random.choice((True, False)))
            else:
                pass
        result.append(element)
    return result

struct = {"num": 20000,"struct": {"bool": {"num": 2}}}
resultList = RandomData(**struct)