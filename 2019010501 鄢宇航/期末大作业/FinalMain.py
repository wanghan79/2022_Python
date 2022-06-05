import math
from functools import wraps
import random

para = {"num": 1, "struct": {"bool": {"datarange": (0, 1)}}}


class RandomNumbers:
    def __init__(self, num):
        self.num = num

    def RandomBool(self):
        ele = []
        res = structDataSampling(**para)[0][0]
        pre = structDataSampling(**para)[0][0]
        ele.append(res)
        ele.append(pre)
        return ele

    def __iter__(self):
        for i in range(self.num):
            yield self.RandomBool()


def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():  # 进入下一层索引
            if key == "int" or "bool":
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
        result.append(element)
    return result


def ACC(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("%s is running" % func.__name__)
        right = func(*args, **kwargs)
        print("ACC is %f" % (int(right) / 10000))
        return right

    return wrapper


def MCC(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("%s is running" % func.__name__)
        exa = func(*args, **kwargs)
        tp = exa[0]
        tn = exa[1]
        fp = exa[2]
        fn = exa[3]
        print("MCC is %f" % ((tp * tn - fp * fn) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))))
        return exa

    return wrapper


@ACC
def pred1(struct):
    right = 0
    for exa in RandomNumbers(10000):
        if exa[0] == exa[1]:
            right = right + 1
    return right


example = []

pred1(example)


@MCC
def pred2(struct):
    fn = tp = fp = tn = 0
    for exa in RandomNumbers(10000):
        if exa[0] == exa[1] == bool(1):
            tp = tp + 1
        if exa[0] == exa[1] == bool(0):
            tn = tn + 1
        if exa[0] != exa[1] == bool(1):
            fp = fp + 1
        if exa[0] == exa[1] == bool(0):
            fn = fn + 1
    return tp, tn, fp, fn


pred2(example)
