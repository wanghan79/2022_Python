import random
from math import sqrt


class _Analysis(object):
    def __init__(self, func, pretype):
        self.__func = func
        self.__pretype = pretype

    def __call__(self, *args, **kwargs):
        results = self.__func(*args, **kwargs)
        if results is None:
            raise Exception("Error! Generated data is None.")
        if self.__pretype == "ACC_Prediction":
            return self.ACC(results)
        elif self.__pretype == "MCC_Prediction":
            return self.MCC(results)

    def ACC(self, data):
        print("This is Acc-Prediction.")
        res = 0
        TP = TN = FP = FN = 0
        for elem in data:
            if elem[0] & elem[1]:
                TP += 1
            elif elem[0] & ~elem[1]:
                TN += 1
            elif ~elem[0] & elem[1]:
                FP += 1
            elif ~elem[0] & ~elem[1]:
                FN += 1
        res = (TP + TN) / (TP + TN + FP + FN)
        return res

    def MCC(self, data):
        print("This is Mcc-Prediction.")
        res = 0
        TP = TN = FP = FN = 0
        for elem in data:
            if elem[0] & elem[1]:
                TP += 1
            elif elem[0] & ~elem[1]:
                TN += 1
            elif ~elem[0] & elem[1]:
                FP += 1
            elif ~elem[0] & ~elem[1]:
                FN += 1
        res = (TP * TN - FP * FN) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        return res


def Analysis(func, pretype):
    def wrapper(function):
        return _Analysis(function, pretype)

    return wrapper


@Analysis("ACC", "ACC_Prediction")
def ACCGenerateRandomData(**kwargs):
    data = list()
    for i in range(0, kwargs['count']):
        element = list()
        for j in range(0, kwargs['num']):
            for key, value in kwargs['struct'].items():
                if key == 'bool':
                    element.append(eval(value))
        data.append(element)
    return data


acc_struct = {'count': 10000, 'num': 2, 'struct': {'bool': 'random.choice([True, False])'}}
acc = ACCGenerateRandomData(**acc_struct)
print(acc)


@Analysis("MCC", "MCC_Prediction")
def MCCGenerateRandomData(**kwargs):
    data = list()
    for i in range(0, kwargs['count']):
        element = list()
        for j in range(0, kwargs['num']):
            for key, value in kwargs['struct'].items():
                if key == 'bool':
                    element.append(eval(value))
        data.append(element)
    return data


mcc_struct = {'count': 10000, 'num': 2, 'struct': {'bool': 'random.choice([True, False])'}}
mcc = MCCGenerateRandomData(**mcc_struct)
print(mcc)

"""
TP: Ture-Positive, TN: True-Negative, FP: False-Positive, FN: False-Negative

Accuracy: 
ACC = (TP + TN) / (TP + TN + FP + FN)

Matthews correlation coefficient:
MCC = (TP * TN - FP * FN) / ((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) ^ 1/2

By RossQAQ - 李长鑫 2020011813, 2022-6-17.
"""
