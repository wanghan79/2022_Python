import random
from functools import wraps
from math import sqrt


def ACC(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        TP = FP = FN = TN = 0
        for item in data:
            if item[0] & item[1]:
                TP += 1
            if item[0] & (~item[1]):
                FP += 1
            if (~item[0]) & item[1]:
                FN += 1
            if (~item[0]) & (item[1]):
                TN += 1
        acc = TP / (TP + FP)
        print("ACC = {}".format(acc))
        return data
    return wrapper

def MCC(res):
    def wrapper(*args, **kwargs):
        data = res(*args, **kwargs)
        TP = FP = FN = TN = 0
        for item in data:
            if item[0] & item[1]:
                TP += 1
            if item[0] & (~item[1]):
                FP += 1
            if (~item[0]) & item[1]:
                FN += 1
            if (~item[0]) & (item[1]):
                TN += 1
        mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC = {}".format(mcc))
        return data
    return wrapper

def structDataSampling(**kwargs):
    result = list()
    for item in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "bool":
                tmp = list()
                for ith in range(value["n"]):
                    element.append(random.choice((True, False)))
            else:
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == "str":
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))

                else:
                    break
                element.append(tmp)
        yield element

@MCC
@ACC
def getData(**kwargs):
    result = list()
    random_num = structDataSampling(**kwargs)
    for i in random_num:
        result.append(i)
    return result


para = {'num': 10000, 'struct': {'bool': {"n": 2}}}
getData(**para)