import random
import math
from functools import wraps


def ACC(calculation):
    def calculation(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            list = func(*args, **kwargs)
            num = len(list)
            count = 0
            for test in list:
                if test[0] == test[1]:
                    count += 1
            print("ACC: {:.2%}".format(count / num))
            return func(*args, **kwargs)
        return wrapper
    return calculation


def MCC(calculation):
    def calculation(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            list = func(*args, **kwargs)
            TP = FP = FN = TN = 0
            for test in list:
                if test[0] == test[1]:
                    if test[0] == 0:
                        TN += 1
                    elif test[0] == 1:
                        TP += 1
                else:
                    if test[0] == 0 and test[1] == 1:
                        FP += 1
                    elif test[0] == 1 and test[1] == 0:
                        FN += 1
            print("MCC : {:.2%}".format((TP * TN - TP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))))
            return func(*args, **kwargs)
        return wrapper
    return calculation


@ACC("calculation")
@MCC("calculation")
def structDataSampling(**kwargs):
    num = kwargs['num']
    result = list()
    for index in range(0, num):
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
                cnt = value['count']
                for i in range(cnt):
                    tmp = random.randint(0, 1)
                    element.append(tmp)
            else:
                element.append("未知类型")
                break
        result.append(element)
    return result


pred = {"num": 100000,"struct": {"bool": {"count": 2},}}
print(structDataSampling(**pred))
