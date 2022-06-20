import random
import math
from math import sqrt
from functools import wraps
import string

def ACC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):
        data = list(fuc(*args, **kwargs))
        print(f"randomDate = {data}")
        num=len(data)
        count = 0
        for i in range(num):
            if data[i][0] == data[i][1]:
                count += 1
        print(f"ACC = {count / num}")
        return data
    return wrap

def MCC(fuc):
    @wraps(fuc)
    def wrap(*args, **kwargs):
        data = list(fuc(*args, **kwargs))
        tp, fp, tn, fn = 0, 0, 0, 0
        for item in data:
            if item[0] & item[1]:
                tp += 1
            elif item[0] & (~item[1]):
                fp += 1
            elif ~item[0] & ~item[1]:
                tn += 1
            elif ~item[0] & item[1]:
                fn += 1
        numerator = (tp * tn) - (fp * fn)
        denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        MCC = numerator / denominator
        print(f"MCC = {MCC}")
        return data
    return wrap

@MCC
@ACC

def StructDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key == 'bool':
                cnt = value['count']
                for i in range(cnt):
                    tmp = random.randint(0, 1)
                    element.append(tmp)
            else:
                print("No!!!!! WrongData")
                break
            element.append(tmp)
        result.append(element)
    return result



Result = {"num": 1000,
        "struct": {"bool": {"count" : 2}}
          }

print(StructDataSampling(**Result))
