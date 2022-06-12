import random
import math
from functools import wraps

#Accuracy指标
def ACC(calculation):
    def calculation(func):
        @wraps(func) #重命名
        def wrapper(*args,**kwargs):

            result = func(*args,**kwargs) #使用list记录func的实验结果
            num = 0
            count = 0 #count记录正确预测数

            while True:
                try:
                    test = next( result )
                    num += 1
                    if (test[0] == test[1]):
                        count += 1
                except StopIteration:
                    break

            print("Accuracy: {:.2%}".format(count / num))
            return func(*args,**kwargs)
        return wrapper
    return calculation

#MCC : 马修斯相关系数
def MCC(calculation):
    def calculation(func):
        @wraps(func)
        def wrapper(*args,**kwargs):

            result = func(*args,**kwargs)
            TP = 0
            FP = 0
            FN = 0
            TN = 0

            while True:
                try:
                    test = next( result )
                    if(test[0] == test[1]):
                        if(test[0] == 0):
                            TN += 1 #真阴性
                        elif(test[0] == 1):
                            TP += 1 #真阳性
                    else:
                        if(test[0] == 0 and test[1] == 1):
                            FP += 1 #假阳性
                        elif(test[0] == 1 and test[1] == 0):
                            FN += 1 #假阴性
                except StopIteration:
                    break

            print("MCC : {:.2%}".format((TP * TN - TP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))))
            return func(*args,**kwargs)
        return wrapper
    return calculation

@MCC("caculation")
@ACC("caculation")
def structDataSampling(**kwargs):
#**kwargs 关键字参数 本质是dist
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
            elif key == 'bool':
                cnt = value['count']
                for i in range(cnt):
                    tmp = random.randint(0,1)
                    element.append(tmp)
            else:
                break
        yield element

pred = {
    "num": 100000,
    "struct": {
        "bool": {"count" : 2},
    }
}

tmp = structDataSampling(**pred)

# while True:
#     try:
#         x = next(tmp)
#         print(x)
#     except StopIteration:
#         break
