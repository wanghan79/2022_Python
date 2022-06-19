import math
import random

class ResultAnalysis():
    def __init__(self,func,static = 'both'):
        self.__func = func
        self.__static = static

    def __call__(self, *args, **kwargs):
        results = self.__func(*args,**kwargs)
        total = len(results)
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
            acc = (TP + TN)/total
            print('ACC : %f' % acc)
        elif self.__static == 'MCC':
            denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            mcc = (TP * TN - FP * FN) / denominator
            print('MCC : %f' % mcc)
        elif self.__static == 'both':  # 没有指定是ACC还是MCC，两个都计算
            acc = (TP + TN) / total
            denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            mcc = (TP * TN - FP * FN) / denominator
            print('ACC : %f;MCC : %f'% (acc,mcc))
        else:
            pass


@ResultAnalysis #计算ACC还是MCC直接修改ResultAnalysis的static变量即可，不修改默认两个都计算
def structDataSampling(**kargs):
    result = list()
    num = kargs["num"]
    struct = kargs["struct"]
    for i in range(0, num):
        element = list()
        for key, value in struct.items():
            if key == 'int':
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == 'float':
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == 'str':
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            elif key == 'bool':
                for j in range(value['datarange']):
                    element.append(random.choice((True, False)))
            else:
                element.append(" ")

        result.append(element)
    return result

data = {"num": 10000, "struct": {"bool": {"datarange": 2}}}
resultList = structDataSampling(**data)