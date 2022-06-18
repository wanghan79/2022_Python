import random
from math import sqrt

def ACC(fun):
    def wrap(*args, **kwargs):
        count,n = 0,0
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
        data = []
        TP, FP, TN, FN = 0, 0, 0, 0
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

@ACC
@MCC
def getRandomData(**keys):
    for i in range(0, keys['num']):
        for key, value in keys['struct'].items():
            if key == "int":
                daterange = iter(value['datarange'])
                yield random.randint(next(daterange), next(daterange))
            elif key == "float":
                daterange = iter(value['datarange'])
                yield random.uniform(next(daterange), next(daterange))
            elif key == "str":
                yield ''.join(random.choice(value['datarange']) for j in range(value['len']))
            elif key == "bool":
                yield [random.choice((True, False)) for ith in range(value["num"])]
            else:
                break


if __name__ == '__main__':
    args = {'num': 1000, 'struct': {'bool': {"num": 2}}}
    format(getRandomData(**args))
