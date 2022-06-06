import random
from functools import wraps
from math import sqrt


def ACC(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        cnt = 0
        data = f(*args, **kwargs)
        for i in range(len(data)):
            if data[i][0] == data[i][1]:
                cnt += 1
        print("ACC = {}".format(cnt / num))
        return data
    return wrap


def MCC(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        data = f(*args, **kwargs)
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
        print("MCC = {}".format(MCC))
        return data
    return wrap



@ACC
def get_ACC_simu(num) -> list:
    ret = []
    for i in range(num):
        item = [random.choice([True, False]), random.choice([True, False])]
        ret.append(item)
    return ret


@MCC
def get_MCC_simu(num) -> list:
    ret = []
    for i in range(num):
        item = [random.choice([True, False]), random.choice([True, False])]
        ret.append(item)
    return ret


num = 10000
get_ACC_simu(num)
get_MCC_simu(num)