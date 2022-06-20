import random
from math import sqrt
from functools import wraps

#ACC
def ACC(decr):
    def calc(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            count = 0
            res = func(*args,**kwargs)
            all = len(res)
            for date in res:
                if date[0] == date[1]:
                    count +=1
            acc = count / all
            print("ACC : {}".format(acc))
            return res
        return wrapper
    return calc

#MCC
def MCC(decr):
    def calc(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)
            TP = FP = FN = TN = 0
            for date in res:
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
            mcc = (TP * TN - FP * FN) / sqrt((TP + FP) * (TP + FP) * (TN + FP) * (TN + FN))
            print("MCC : {}".format(mcc))
            return res
        return wrapper
    return calc

@ACC("ACC")
@MCC("MCC")
def structDateSampling(**kwargs):
    result = list()
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
        result.append(element)
    return result

def apply():
    para = {"num": 10000, "struct": {"bool": {"count": 2}} }
    format(structDateSampling(**para))

apply()