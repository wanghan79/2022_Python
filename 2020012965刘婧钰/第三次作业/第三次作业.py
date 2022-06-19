"""
    Author:  Liu
    Purpose: pass.
    Created: 6/18/2022
"""

import random
from math import sqrt


class resultAnalysis(object):
    def __init__(self, func, static):
        self.__func = func
        self.__static = static

    def __call__(self, *args, **kwargs):
        results = self.__func(*args, **kwargs)
        if results is None:
            raise Exception("Error! Generated data is None.")
        if self.__static == "ACCPrediction":
            return self.ACC(results)
        elif self.__static == "MCCPrediction":
            return self.MCC(results)

    def ACC(self, data):
        print("This is Acc:")
        result = 0
        truePositive = trueNegative = falsePositive = falseNegative = 0
        for item in data:
            if item[0] & item[1]:
                truePositive += 1
            elif item[0] & ~item[1]:
                trueNegative += 1
            elif ~item[0] & item[1]:
                falsePositive += 1
            elif ~item[0] & ~item[1]:
                falseNegative += 1
        result = (truePositive + trueNegative) / (truePositive + trueNegative + falsePositive +falseNegative)
        return result

    def MCC(self, data):
        print("This is Mcc:")
        result = 0
        truePositive = trueNegative = falsePositive = falseNegative = 0
        for item in data:
            if item[0] & item[1]:
                truePositive += 1
            elif item[0] & ~item[1]:
                trueNegative += 1
            elif ~item[0] & item[1]:
                falsePositive += 1
            elif ~item[0] & ~item[1]:
                falseNegative += 1
        result = (trueNegative * trueNegative - falsePositive * falseNegative) / sqrt((truePositive + falsePositive) * (truePositive + falseNegative) * (trueNegative + falsePositive) * (trueNegative + falseNegative))
        return result


def ResultAnalysis(func, static):
    def wrapper(function):
        return resultAnalysis(function, static)

    return wrapper


@ResultAnalysis("ACC", "ACCPrediction")
def ACCDataSampling(**kwargs):
    data = list()
    for index in range(0, kwargs['count']):
        element = list()
        for item in range(0, kwargs['num']):
            for key, value in kwargs['struct'].items():
                if key == 'bool':
                    element.append(eval(value))
        data.append(element)
    return data



@ResultAnalysis("MCC", "MCCPrediction")
def MCCDataSampling(**kwargs):
    data = list()
    for index in range(0, kwargs['count']):
        element = list()
        for item in range(0, kwargs['num']):
            for key, value in kwargs['struct'].items():
                if key == 'bool':
                    element.append(eval(value))
        data.append(element)
    return data


acc_struct = {'count': 10000, 'num': 3, 'struct': {'bool': 'random.choice([True, False])'}}
acc = ACCDataSampling(**acc_struct)
print(acc)
mcc_struct = {'count': 10000, 'num': 3, 'struct': {'bool': 'random.choice([True, False])'}}
mcc = MCCDataSampling(**acc_struct)
print(mcc)