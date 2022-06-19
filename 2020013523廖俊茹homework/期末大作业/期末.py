'''
ACC OR MCC :
just change the value of 'static'
'''
import random
import math

#实现yield
class randomYield:
    def __init__(self,num, **kwargs):
        self.num1 = num
        self.kwargs1 = kwargs

    def __iter__(self):
        for i in range(self.num1):
            if i == self.num1:
                raise StopIteration
            element = list()
            for key, value in self.kwargs1.items():
                if key == 'int':
                    it = iter(value['datarange'])
                    element.append(random.randint(next(it), next(it)))
                elif key == 'float':
                    it = iter(value['datarange'])
                    element.append(random.uniform(next(it), next(it)))
                elif key == 'str':
                    element.append(
                        ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
                elif key == 'bool':
                    for m in range(value['datarange']):
                        element.append(random.choice((True, False)))
                else:
                    break
            yield element
#类修饰器
class ResultAnalysis():
    def __init__(self,func,static = 'both'):#此处更改static为’ACC‘实现另一种修饰功能
        self.func1 = func
        self.static1 = static
    def __call__(self, *args, **kwargs):
        results = self.func1(*args,**kwargs)
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
            acc = (TP + TN) / total
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
def getRandoms(**kwargs):
    generator = randomYield(10000,**kwargs)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList

argument = {'bool':{'datarange':2}}
relistList = getRandoms(**argument)