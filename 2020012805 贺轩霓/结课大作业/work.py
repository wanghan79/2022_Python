import random
from math import sqrt


class StructDataSampling:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for index in range(0, self.num):
            tmp = list()
            for key, value in self.struct.items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == "str":
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(self.num))
                elif key == "bool":
                    for i in range(value["datarange"]):
                        tmp.append(random.choice((True, False)))
                else:
                    break
            yield tmp


def ACC(func):
    def wrap(*args, **kwargs):
        count = 0
        data = func(*args, **kwargs)
        n = len(data)
        for i in range(n):
            if data[i][0] == data[i][1]:
                count += 1
        acc = count / n
        print("ACC = %f" % acc)
        return data

    return wrap


def MCC(func):
    def wrap(*args, **kwargs):
        data = func(*args, **kwargs)
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
def structDataSampling():
    struct = {"num": 1000, "struct": {"bool": {'datarange': 2}}}
    generator = StructDataSampling(**struct)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList


structDataSampling()
