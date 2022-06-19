'''
ACC OR MCC :
just change the value of 'static'
ps:老师，ResultAnalysis('ACC')好像不能这么用
'''
#-*-encoding:utf-8-*-
import math
import random
class ResultAnalysis():
    def __init__(self,func,static = 'both'):
        self.func1 = func
        self.static1 = static
    def __call__(self, *args, **kwargs):
        results = self.func1(*args,**kwargs)
    #     if results is None:
    #         return None
    #     else:
    #         return self.Precision(results)
    #
    # def Precision(self,data):#利用随机数生成函数产生多个随机数，用计算公式算出最后精确度
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
        if self.static1 == 'ACC':
            acc = (TP + TN)/total
            print('ACC : %f' % acc)
        elif self.static1 == 'MCC':
            denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            mcc = (TP * TN - FP * FN) / denominator
            print('MCC : %f' % mcc)
        elif self.static1 == 'both':#ACC and MCC share a set of data
            acc = (TP + TN) / total
            denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            mcc = (TP * TN - FP * FN) / denominator
            print('ACC : %f;MCC : %f'% (acc,mcc))
        else:
            pass


@ResultAnalysis #计算ACC还是MCC直接修改ResultAnalysis的static变量即可
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
resultList = structDataSampling(10000,**struct)