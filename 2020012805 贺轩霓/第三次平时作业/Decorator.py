import random
from math import sqrt


def ACC(fun):
    def wrap(*args, **kwargs):
        count = 0
        data = fun(*args, **kwargs)
        n = len(data)
        for i in range(n):
            if data[i][0] == data[i][1]:
                count += 1
        acc = count / n
        print("ACC = %f" % acc)
        return data
    return wrap


def MCC(fun):
    def wrap(*args, **kwargs):
        data = fun(*args, **kwargs)
        TP = FP = TN = FN = 0
        for i in data:
            if i[0] & i[1]:
                TP += 1
            elif i[0] & (~i[1]):
                FP += 1
            elif ~i[0] & ~i[1]:
                TN += 1
            elif ~i[0] & i[1]:
                FN += 1
        mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC = %f" % mcc)
        return data
    return wrap


@MCC
@ACC
def structDataSampling(num, *args, **kwargs):
    results = list()
    for index in range(0, num):
        tmp = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(num))
            elif key == "bool":
                for i in range(value["datarange"]):
                    tmp.append(random.choice((True, False)))
            else:
                break
            results.append(tmp)
    return results


struct = {"bool": {'datarange': 2}}
result = structDataSampling(1000, **struct)
