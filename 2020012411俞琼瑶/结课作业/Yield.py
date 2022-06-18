"""
    Author: yqy
    Created: 2022/6/4 10:20
"""
import random
from functools import wraps
from math import sqrt


def ACC(decPara):
    def decorator(func):
        # 重命名，让被修饰函数的函数名不被改变为wrapper
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 0  # count记录正确数量
            total = 0  # total记录总数量
            data = func(*args, **kwargs)
            while True:
                try:
                    i = next(data)
                    total += 1
                    if i[0] == i[1]:
                        count += 1
                except StopIteration:
                    break
            if total == 0:
                acc = 0
            else:
                acc = count / total
            print("ACC = {:.2%}".format(acc))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def MCC(decPara):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            TP, FP, TN, FN = 0, 0, 0, 0
            while True:
                try:
                    i = next(data)
                    if i[0] & i[1]:
                        TP += 1
                    elif i[0] & (~i[1]):
                        FP += 1
                    elif ~i[0] & ~i[1]:
                        TN += 1
                    elif ~i[0] & i[1]:
                        FN += 1
                except StopIteration:
                    break
            if sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) == 0:
                mcc = 0
            else:
                mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            print("MCC = {:.2%}".format(mcc))
            return data
            # return func(*args, **kwargs)  # 使用该句会计算2次ACC
        return wrapper
    return decorator


@MCC("MCC")
@ACC("ACC")
def structDataSampling(**kwargs):
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
                element.append(tmp)
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
                element.append(tmp)
            elif key == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                element.append(tmp)
            elif key == 'bool':
                for ith in range(value['count']):
                    tmp = random.randint(0, 1)
                    element.append(tmp)
            else:
                break
        yield element


para = {'num': 1000, 'struct': {'bool': {'count': 2}}}
print(structDataSampling(**para))
