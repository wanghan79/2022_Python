import random
from math import sqrt
from functools import wraps
import string

def ACC(f):
    def wrap(*args, **kwargs):
        cnt = 0
        data = f(*args, **kwargs)
        n = len(data)
        for i in range(n):
            if data[i][0] == data[i][1]:
                cnt += 1
        acc = cnt / n
        print("ACC = {}".format(acc))
        return data
    return wrap

def MCC(f):
    def wrap(*args, **kwargs):
        data = f(*args, **kwargs)
        TP,  FP, TN, FN = 0, 0, 0, 0
        for i in data:
            if i[0] & i[1]:
                TP += 1
            elif i[0] & (~i[1]):
                FP += 1
            elif (~i[0]) & (~i[1]):
                TN += 1
            elif (~i[0]) & i[1]:
                FN += 1
        mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TN + FN) * (TP + FN) * (FP + TN))
        print("MCC = {}".format(mcc))
        return data
    return wrap

@ACC
@MCC
def structDataSampling(num, **kwargs):
    for index in range(0, num):
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                yield random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                yield random.uniform(next(it), next(it))
            elif key == "str":
                yield ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key == "bool":
                yield [random.choice((True, False)) for _ in range(value["num"])]
            else:
                break

if __name__ == '__main__':
    para = {'num': 1000, 'struct': {'bool': {"num": 2}}}
    print("randomData:{}".format(structDataSampling(**para)))
