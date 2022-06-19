import random
from functools import wraps
import math
import string

def ResultAnalysis(flag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            total = 10000
            TP = TN = FP = FN = 0
            for elm in result:
                if(elm[0] >= 50) and (elm[1] >= 5000.0):
                    TP += 1
                elif(elm[0] >= 50) and (elm[1] < 5000.0):
                    FN += 1
                elif (elm[0] < 50) and (elm[1] >= 5000.0):
                    FP += 1
                elif (elm[0] < 50) and (elm[1] < 5000.0):
                    TN += 1
                else:
                    pass
            if flag == "ACC":
                acc = (TP + TN) / total
                print(acc)
            elif flag =="MCC":
                de = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                if(de == 0):
                    de = 1
                mcc = (TP * TN - FP * FN) / de
                print(mcc)
            else:
                pass
            return result
        return wrapper
    return decorator



struct = {"int": {"datarange": [0, 100]}, "float": {"datarange": [0, 10000]}, "str": {"datarange": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "len": 10}}

@ResultAnalysis("ACC")
def StructDataSampling(num,**kwargs):

    for index in range(0,num):
        element = list()
        for key,value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it),next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it),next(it)))
            elif key == "str":
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            else:
                element.append("None")
        yield element

StructDataSampling(10000,**struct)

@ResultAnalysis("MCC")
def StructDataSampling(num,**kwargs):

    for index in range(0,num):
        element = list()
        for key,value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it),next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it),next(it)))
            elif key == "str":
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            else:
                element.append("None")
        yield element

StructDataSampling(10000,**struct)


