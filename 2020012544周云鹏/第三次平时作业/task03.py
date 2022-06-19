"""
   Author: Zhou
   Purpose: Python task 03
   Created: {2022/6/10}
"""
import random
from math import sqrt
from functools import wraps
# Step1  Constructs a class decorator function
class ResultAnalysis:
    def __init__(self,static = "ACC"):
        self.__static= static
    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def wrapper(**kwargs):
            results =func(**kwargs)
            if results is None:
                return None
            if self.__static=="ACC":
                 self.ACC(results)
            elif self.__static=="MCC":
                 self.MCC(results)
            return results
        return wrapper

    def ACC(self,results):
        n = len(results)
        count = 0
        for i in range(n):
            if results[i][0] == results[i][1]:
                count += 1
        acc = count / n
        print("ACC = {}".format(acc))

    def MCC(self,results):
        TP, FP, TN, FN = 0, 0, 0, 0
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
        mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC = {}".format(mcc))

# Step2 A random number generating function is constructed and decorated with ACC and MCC
@ResultAnalysis("MCC")
@ResultAnalysis("ACC")
def structDataSampling(**kwargs):
    result = list()
    for index in range(0,kwargs['num']):
        element = list()
        for key,value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it),next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it),next(it)))
            elif key == "str":
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen'])))
            elif key == "Analysis":
                for ith in range(value["number"]):
                 element.append(random.choice((True, False)))
            else:
                break
        result.append(element)
    return result
# Step3 Run, generating ACC and MCC
dic = {"num": 10000, "struct": {"Analysis": {"number": 2}}}
structDataSampling(**dic)