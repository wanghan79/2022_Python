"""
Author: WanshunSu 2020012972
Purpose: Final python class homework in spring semester, 2022
Introduction:
           A class for calculate ACC and MCC,It is implemented using decorator.
           It and 'Random_Generator_Class_Decorator.py' and 'test.py' are a whole,The purpose is
           to calculate ACC and MCC of randomly generated groups of Boolean data.
           If you want to test this class and 'Random_Generator_Class_Iterator.py', Please run 'test.py',
           'Random_Generator' in the 'test.py' file tests this class and 'Random_Generator_Class_Iterator.py'.
Created:2022/6/3
"""
import math
from functools import wraps

class ACC_MCC_Decorator:
    '''

    '''
    def __init__(self, static="ACC"):
        self.__static = static

    def __call__(self, func, *args, **kwargs):
            @wraps(func)
            def wrapper(*args, **kwargs):
                results = func(*args, **kwargs)
                if self.__static == "ACC":
                    self.ACC(results)
                elif self.__static == "MCC":
                    self.MCC(results)
                return results
            return wrapper

    def Parameter(self,rseults):
        total = len(rseults)
        TP = TN = FP = FN = 0
        for a in rseults:
            if (a[0] is True) and (a[1] is True):
                TP += 1
            elif (a[0] is True) and (a[1] is False):
                FN += 1
            elif (a[0] is False) and (a[1] is True):
                FP += 1
            elif (a[0] is False) and (a[1] is False):
                TN += 1
        return TP, FN, FP, TN, total

    def ACC(self,results):
        TP, FN, FP, TN, total = self.Parameter(results)
        ACC = (TP + TN) / total
        print("ACC is %f" % ACC)

    def MCC(self, results):
        TP, FN, FP, TN, total = self.Parameter(results)
        MCC = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC is %f" % MCC)