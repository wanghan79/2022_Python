from functools import wraps
import random
import math

def ACC(calculation):
    def calculation(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            list = func(*args,**kwargs)
            num = len(list)
            moment = 0
            for test in list:
                if test[0] == test[1]:
                    moment += 1
            print("Accuracy: {:.2%}".format(moment / num))
            return func(*args , **kwargs)
        return wrapper
    return calculation

def MCC(calculation):
    def calculation(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            list = func(*args,**kwargs)
            X = Y = z = M = 0
            for test in list:
                if(test[0] == test[1]):
                    if(test[0] == 1):
                        X += 1
                    elif(test[0] == 0):
                        M += 1
                else:
                    if(test[0] == 0 and test[1] == 1):
                        Y += 1
                    elif(test[0] == 1 and test[1] == 0):
                        z += 1
            print("MCC : {:.2%}".format((X * M - X * z) / math.sqrt((X + Y) * (X + z) * (M + Y) * (M + z))))
            return func(*args,**kwargs)
        return wrapper
    return calculation

@ACC("calculation")
@MCC("calculation")
def structDataSampling(**kwargs):
    """
    :param num:
    :param struct:
    :return:
    """
    num = kwargs['num']
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                I = iter(value['datarange'])
                T = random.randint(next(I), next(I))
                element.append(T)
            elif key == "float":
                it = iter(value['datarange'])
                T = random.uniform(next(I), next(I))
                element.append(T)
            elif key == "str":
                T = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                element.append(T)
            elif key == 'bool':
                cnt = value['count']
                for i in range(cnt):
                    T = random.randint(0,1)
                    element.append(T)
            else:
                break
        result.append(element)
    return result

pred = {
    "num": 999999,
    "struct": {
        "bool": {"count" : 2},
    }
}

print(structDataSampling(**pred))
