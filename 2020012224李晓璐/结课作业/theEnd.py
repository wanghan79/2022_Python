import random
from math import sqrt
from functools import wraps

#Accuracy准确度
def ACC(call):
    def calc(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            count = all = 0
            res = func(*args,**kwargs)
            while True:
                try:
                    date = next(res)
                    all += 1
                    if date[0] == date[1]:
                        count += 1
                except StopIteration:
                    break
            acc = count / all
            print("ACC : {}".format(acc))
            return res
        return wrapper
    return calc

#Mcc马修斯相关系数
def MCC(call):
    def calc(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)
            TP = FP = FN = TN = 0
            while True:
                try:
                    date = next(res)
                    if (date[0] == False):
                        if (date[1] == False): #0 0
                            TN += 1
                        elif (date[1] == True): #0 1
                             FN += 1
                    elif (date[0] == True):
                        if (date[1] == False): #1 0
                            FP += 1
                        elif (date[1] == True): #1 1
                            TP += 1
                except StopIteration:
                    break
            mcc = (TP * TN - FP * FN) / sqrt((TP + FP) * (TP + FP) * (TN + FP) * (TN + FN))
            print("MCC : {}".format(mcc))
            return func(*args,**kwargs)
        return wrapper
    return calc

#随机数
@ACC("ACC")
@MCC("MCC")
def structDateSampling(**kwargs):
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
                element.append(tmp)
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
                element.append(tmp)
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                element.append(tmp)
            elif key == "bool":
                for i in range(value["count"]):
                    tmp = random.randint(0,1)
                    element.append(tmp)
            else:
                break
        yield element

def apply():
    para = {"num": 1000, "struct": {"bool": {"count": 2}} }
    format(structDateSampling(**para))

apply()
