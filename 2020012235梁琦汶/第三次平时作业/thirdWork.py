"""
 Author:CreamCheese
 purpose:pass
 created:2022/6/20 00:04
"""
import random
from functools import wraps
import math


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
def getRandomData(**keys):
    samples = []
    for i in range(0, keys['num']):
        sample = []
        for key, value in keys['struct'].items():
            if key == "int":
                daterange = iter(value['datarange'])
                sample.append(random.randint(next(daterange), next(daterange)))
            elif key == "float":
                daterange = iter(value['datarange'])
                sample.append(random.uniform(next(daterange), next(daterange)))
            elif key == "str":
                sample.append(''.join(random.choice(value['datarange']) for i in range(value['len'])))
            elif key == "bool":
                for ith in range(value["num"]):
                    sample.append(random.choice((True, False)))
            else:
                break
        samples.append(sample)
    return samples


def main():
    struct = {'num': 10000, 'struct': {'bool': {"num": 2}}}
    format(getRandomData(**struct))



if __name__ == '__main__':

    main()
