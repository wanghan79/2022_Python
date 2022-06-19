import random
from functools import wraps
from math import sqrt


def MCC(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        dataList = func(*args, **kwargs)
        TP, FP, TN, FN = 0, 0, 0, 0
        for data in dataList:
            if data[0] & data[1]:
                TP += 1
            elif data[0] & (~data[1]):
                FP += 1
            elif ~data[0] & ~data[1]:
                TN += 1
            elif ~data[0] & data[1]:
                FN += 1
        mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC = {}".format(mcc))
        return dataList

    return wrap


def ACC(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        count = 0
        data = func(*args, **kwargs)
        n = len(data)
        for i in range(n):
            if data[i][0] == data[i][1]:
                count += 1
        acc = count / n
        print("ACC = {}".format(acc))
        return data

    return wrap


@MCC
@ACC
def getRandomData(**kwargs):
    samples = []
    for i in range(0, kwargs['num']):
        sample = []
        for key, value in kwargs['struct'].items():
            if key == "int":
                dataRange = iter(value['dataRange'])
                sample.append(random.randint(next(dataRange), next(dataRange)))
            elif key == "float":
                dataRange = iter(value['dataRange'])
                sample.append(random.uniform(next(dataRange), next(dataRange)))
            elif key == "str":
                sample.append(''.join(random.choice(value['dataRange']) for i in range(value['len'])))
            elif key == "bool":
                for ith in range(value["num"]):
                    sample.append(random.choice((True, False)))
            else:
                break
        samples.append(sample)
    return samples


if __name__ == '__main__':
    args = {'num': 1000, 'struct': {'bool': {"num": 2}}}
    dataList = getRandomData(**args)
