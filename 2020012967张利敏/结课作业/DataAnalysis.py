import math
import random
from functools import wraps


def MCC(data):
    TP = TN = FP = FN = 0
    for i in data:
        if (i[0] is True) and (i[1] is True):
            TP += 1
        elif (i[0] is True) and (i[1] is False):
            FN += 1
        elif (i[0] is False) and (i[1] is False):
            FP += 1
        elif (i[0] is False) and (i[1] is False):
            TN += 1
        else:
            pass
    res = math.sqrt((TP + FP)*(TP+FN)*(TN+FP)*(TN+FN))
    if res ==0:
        res = 1
    mcc = (TP * TN - FP * FN) / res
    print("mcc:", mcc)

def ACC(data):
    TP=TN= FP= FN =0
    sum = 0
    for i in data:
        if (i[0] is True) and (i[1] is True):
            TP += 1
        elif (i[0] is True) and (i[1] is False):
            FN += 1
        elif (i[0] is False) and (i[1] is False):
            FP += 1
        elif (i[0] is False) and (i[1] is False):
            TN += 1
        else:
            pass
        sum += 1
    acc = (TP + TN) / sum
    print("acc:",acc)

def add_func(type):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            if type =="ACC":
                data = func(*args, **kwargs)
                ACC(data)
            elif type == "MCC":
                data = func(*args, **kwargs)
                MCC(data)
        return wrapped_function
    return logging_decorator

@add_func("ACC")
def structDataSampling(num, **kwargs):
    for index in range(0, num):
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key == "bool":
                bool_num = []
                for i in range(value["num"]):
                    bool_num.append(random.choice((True,False)))
            #     tmp = bool_num
            # element.append(tmp)
        yield bool_num

data = {"num":10000,"bool":{"num":20}}
structDataSampling(**data)

@add_func("MCC")
def structDataSampling(num, **kwargs):
    for index in range(0, num):
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key == "bool":
                bool_num = []
                for i in range(value["num"]):
                    bool_num.append(random.choice((True,False)))
            #     tmp = bool_num
            # element.append(tmp)
        yield bool_num

data = {"num":10000,"bool":{"num":20}}
structDataSampling(**data)