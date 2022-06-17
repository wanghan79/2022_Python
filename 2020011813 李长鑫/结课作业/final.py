import random
from math import sqrt


class _Analysis(object):
    def __init__(self, func, pretype):
        self.__func = func
        self.__pretype = pretype
        self.acc = 0
        self.mcc = 0

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
        TP = TN = FP = FN = 0
        for it in data:
            for elem in it:
                if elem[0] & elem[1]:
                    TP += 1
                elif elem[0] & ~elem[1]:
                    TN += 1
                elif ~elem[0] & elem[1]:
                    FP += 1
                elif ~elem[0] & ~elem[1]:
                    FN += 1
        self.acc = (TP + TN) / (TP + TN + FP + FN)
        return self.acc

    def MCC(self, data):
        print("This is Mcc-Prediction.")
        TP = TN = FP = FN = 0
        for it in data:
            for elem in it:
                if elem[0] & elem[1]:
                    TP += 1
                elif elem[0] & ~elem[1]:
                    TN += 1
                elif ~elem[0] & elem[1]:
                    FP += 1
                elif ~elem[0] & ~elem[1]:
                    FN += 1
        self.mcc = (TP * TN - FP * FN) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        return self.mcc


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
    yield data


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
    yield data


mcc_struct = {'count': 10000, 'num': 2, 'struct': {'bool': 'random.choice([True, False])'}}
mcc = MCCGenerateRandomData(**mcc_struct)
print(mcc)
