"""
  Author: Wenqian Chen
  Purpose:pass.
  Created:{Date}
"""
import random
import math


class resultAnalysis():
    """
        DESCRIPTION: This class is a decorator using the popular methods to analysis the results generated
                     by the function who was decorated
        """
    def __init__(self, func, static):
        self.__func = func
        self.__static = static

    def __call__(self, *args, **kwargs):
        results = self.__func(*args, **kwargs)    #result 应该对应随机数生成结果数据
        if results is None:
            return None
        if self.__static == "ACC":
            return self.ACC(results)
        elif self.__static == "MCC":
            return self.MCC(results)

    def ACC(self, data):
        print('ACC : ' )
        TP = TN = FP = FN = 0
        for i in data:
            if (i[0] is True) and (i[1] is True):
                TP += 1
            elif (i[0] is True) and (i[1] is False):
                FN += 1
            elif (i[0] is False) and (i[1] is True):
                FP += 1
            elif (i[0] is False) and (i[1] is False):
                TN += 1
        result = (TP + TN) / (TP + FN + FP + TN)
        return result

    def MCC(self, data):
        print('MCC :' )
        TP = TN = FP = FN = 0
        for i in data:
            if (i[0] is True) and (i[1] is True):
                TP += 1
            elif (i[0] is True) and (i[1] is False):
                FN += 1
            elif (i[0] is False) and (i[1] is True):
                FP += 1
            elif (i[0] is False) and (i[1] is False):
                TN += 1
        numerator = (TP * TN - FP * FN)
        denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        result = numerator / denominator
        return result


def ResultAnalysis(func, static):
    def wrapper(function):
        return resultAnalysis(function, static)

    return wrapper


@ResultAnalysis("ACC", "ACC")
def ACCstructDataSampling(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == 'int':
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == 'float':
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == 'str':
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            elif key == 'bool':
                for m in range(value['datarange']):
                    element.append(random.choice((True, False)))
            else:
                break

        result.append(element)
    return result



@ResultAnalysis("MCC", "MCC")
def MCCstructDataSampling(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == 'int':
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == 'float':
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == 'str':
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            elif key == 'bool':
                for m in range(value['datarange']):
                    element.append(random.choice((True, False)))
            else:
                break

        result.append(element)
    return result


struct = {'bool':{'datarange':2}}
acc = ACCstructDataSampling(10000,**struct)
print(acc)
mcc = MCCstructDataSampling(10000,**struct)
print(mcc)
