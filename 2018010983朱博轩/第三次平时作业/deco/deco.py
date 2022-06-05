from functools import wraps
from math import sqrt


def ACC(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        currect = 0
        for real, pred in res:
            if real == pred:
                currect += 1
        return currect / len(res)

    return wrapper


def MCC(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for real, pred in res:
            if real == 1:
                if real == pred:
                    tp += 1
                else:
                    fn += 1
            else:
                if real == pred:
                    tn += 1
                else:
                    fp += 1
        return (tp * tn - fp * fn) / (max(
            sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)), 1))

    return wrapper