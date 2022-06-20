from functools import wraps
import random
import math

def ACC(calculation):
    def calculation(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            n= m = 0
            while True:
                try:
                    test = next( result )
                    n += 1
                    if (test[0] == test[1]):
                        m += 1
                except StopIteration:
                    break

            print("Accuracy: {:.2%}".format(m / n))
            return func(*args , **kwargs)
        return wrapper
    return calculation

def MCC(calculation):
    def calculation(func):
        @wraps(func)
        def wrapper(*args,**kwargs):

            result = func(*args,**kwargs)
            X = Y = Z = R = 0
            while True:
                try:
                    test = next( result )
                    if(test[0] == test[1]):
                        if(test[0] == 0):
                            R += 1
                        elif(test[0] == 1):
                            X += 1
                    else:
                        if(test[0] == 0 and test[1] == 1):
                            Y += 1
                        elif(test[0] == 1 and test[1] == 0):
                            Z += 1
                except StopIteration:
                    break

            print("MCC : {:.2%}".format((X * R - X * Z) / math.sqrt((X + Y) * (X + Z) * (R + Y) * (R + Z))))
            return func(*args,**kwargs)
        return wrapper
    return calculation

@MCC("caculation")
@ACC("caculation")
def structDataSampling(**kwargs):
    """
    :param num:
    :param struct:
    :return:
    """
    num = kwargs['num']
    for index in range(0, num):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                I = iter(value['datarange'])
                T = random.randint(next(I), next(I))
                element.append(T)
            elif key == "float":
                I = iter(value['datarange'])
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
        yield element

pred = {
    "num": 999999,
    "struct": {
        "bool": {"count" : 2},
    }
}
T = structDataSampling(**pred)
