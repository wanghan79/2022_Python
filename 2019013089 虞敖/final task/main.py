from functools import wraps
from math import sqrt
from randoom import Random


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
def get_ACC_simu(**kwargs) -> list:
    ret = []
    random_generator = Random(**kwargs)
    for i in random_generator:
        ret.append(i)
    return ret


@MCC
def get_MCC_simu(**kwargs) -> list:
    ret = []
    random_generator = Random(**kwargs)
    for i in random_generator:
        ret.append(i)
    return ret


num = 1000
random_para = {"num": num, "struct": {"bool": {"num": 2}}} #

get_ACC_simu(**random_para)
get_MCC_simu(**random_para)
