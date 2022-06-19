"""
  Author: Wenqian Chen
  Purpose:pass.
  Created:{Date}
"""
import math
import random
class ResultAnalysis():
    """
        DESCRIPTION: This class is a decorator using the popular methods to analysis the results generated
                     by the function who was decorated
        """

    def __init__(self, func, static="ACC&MCC"):
        self.__func = func
        self.__static = static
    def __call__(self, *args, **kwargs):
        results = self.__func(*args,**kwargs)   #result 应该对应随机数生成结果数据
        TP = TN = FP = FN = 0
        for i in results:
            if (i[0] is True) and (i[1] is True):
                TP += 1
            elif (i[0] is True) and (i[1] is False):
                FN += 1
            elif (i[0] is False) and (i[1] is True):
                FP += 1
            elif (i[0] is False) and (i[1] is False):
                TN += 1
            else:
                pass
        if self.__static == 'ACC':
            acc = (TP + TN)/(TP+FN+FP+TN)
            print('ACC : %f' % acc)
        elif self.__static == 'MCC':
            numerator = (TP * TN - FP * FN)
            denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            mcc = numerator/ denominator
            print('MCC : %f' % mcc)
        elif self.__static == "ACC&MCC":
            acc = (TP + TN) / (TP+FN+FP+TN)
            numerator = (TP * TN - FP * FN)
            denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            mcc = numerator / denominator
            print('ACC : %f;MCC : %f' % (acc, mcc))
        else:
            pass


@ResultAnalysis
def structDataSampling(num, **kwargs):
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
result = structDataSampling(10000,**struct)