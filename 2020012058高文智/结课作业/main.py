import random
from math import sqrt

'''
改写平时作业三，采用生成器方式生成相应随机数
'''


def ACC(func):
    def wrap(*args, **kwargs):
        data = []
        count = total = 0
        for i in func(*args, **kwargs):
            data.append(i)
            if i[0] == i[1]:
                count += 1
            total += 1
        print(f"ACC = {count / total}")
        return data

    return wrap


def MCC(func):
    def wrap(*args, **kwargs):
        data = []
        tp = fp = tn = fn = 0
        for i in func(*args, **kwargs):
            data.append(i)
            if i[0] & i[1]:
                tp += 1
            elif i[0] & (~i[1]):
                fp += 1
            elif ~i[0] & ~i[1]:
                tn += 1
            elif ~i[0] & i[1]:
                fn += 1
        MCC = (tp * tn) - (fp * fn) / sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        print(f"MCC = {MCC}")
        return data

    return wrap


@MCC
@ACC
def get_random_data(**keys):
    for i in range(0, keys['num']):
        for key, value in keys['struct'].items():
            if key == "int":
                daterange = iter(value['datarange'])
                yield random.randint(next(daterange), next(daterange))
            elif key == "float":
                daterange = iter(value['datarange'])
                yield random.uniform(next(daterange), next(daterange))
            elif key == "str":
                yield ''.join(random.choice(value['datarange']) for _ in range(value['len']))
            elif key == "bool":
                yield [random.choice((True, False)) for _ in range(value["num"])]
            else:
                break


para = {'num': 10000, 'struct': {'bool': {"num": 2}}}
get_random_data(**para)
