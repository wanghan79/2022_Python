import random
from functools import wraps
import math


def structDataSampling(**kwargs):
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
                element.append(tmp)
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
                element.append(tmp)
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                element.append(tmp)
            elif key == 'bool':
                cnt = value['num']
                for i in range(cnt):
                    element.append(random.choice((True, False)))
            else:
                pass
        yield element


def decorate(flag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
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
            if flag == "ACC":
                acc = (TP + TN) / total
                print("ACC : %f" % acc)
            elif flag == "MCC":
                denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                mcc = (TP * TN - FP * FN) / denominator
                print("MCC : %f" % mcc)
            return result

        return wrapper

    return decorator


@decorate("MCC")
@decorate("ACC")
def random_data(**kwargs):
    data_sampling = structDataSampling(**kwargs)
    result_list = []
    for data in data_sampling:
        result_list.append(data)
    return result_list


struct = {"num": 20000,"struct": {"bool": {"num": 2}}}
resultList = random_data(**struct)
for elem in resultList:
    print(elem)