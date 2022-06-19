import random
from math import sqrt


def ACC(fun):
    def wrap(*args, **kwargs):
        count, n = 0, 0
        data = []
        for i in fun(*args, **kwargs):
            data.append(i)
            if i[0] == i[1]:
                count += 1
            n += 1
        acc = count / n
        print("ACC = {}".format(acc))
        return data

    return wrap


def MCC(fun):
    def wrap(*args, **kwargs):
        TP, FP, TN, FN = 0, 0, 0, 0
        data = []
        for i in fun(*args, **kwargs):
            data.append(i)
            if i[0] & i[1]:
                TP += 1
            elif i[0] & (~i[1]):
                FP += 1
            elif ~i[0] & ~i[1]:
                TN += 1
            elif ~i[0] & i[1]:
                FN += 1
        mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC = {}".format(mcc))
        return data

    return wrap


@MCC
@ACC
def getRandomData(**kwargs):
    for i in range(0, kwargs['num']):
        for key, value in kwargs['struct'].items():
            if key == "int":
                dataRange = iter(value['datarange'])
                yield random.randint(next(dataRange), next(dataRange))
            elif key == "float":
                dataRange = iter(value['datarange'])
                yield random.uniform(next(dataRange), next(dataRange))
            elif key == "str":
                yield ''.join(random.choice(value['datarange']) for i in range(value['len']))
            elif key == "bool":
                yield [random.choice((True, False)) for _ in range(value["num"])]
            else:
                break


args = {'num': 1000, 'struct': {'bool': {"num": 2}}}
dataJudge = getRandomData(**args)
