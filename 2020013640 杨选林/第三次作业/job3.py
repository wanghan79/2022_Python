import math
import random
from functools import wraps

#Accuracy指标
def ACC(calculation):
    def calculation(func):
        @wraps(func) #重命名
        def wrapper(*args,**kwargs):
            list = func(*args,**kwargs) #使用list记录func的实验结果
            num = len(list)
            count = 0 #count记录正确预测数量
            for test in list:
                if test[0] == test[1]:
                    count += 1
            print("Accuracy: {:.2%}".format(count / num))
            return func(*args,**kwargs)
        return wrapper
    return calculation

#MCC : 马修斯相关系数
def MCC(calculation):
    def calculation(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            list = func(*args,**kwargs)
            TP = 0
            FP = 0
            FN = 0
            TN = 0
            for test in list:
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
            print("MCC : {:.2%}".format((TP * TN - TP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))))
            return func(*args,**kwargs)
        return wrapper
    return calculation

@ACC("calculation")
@MCC("calculation")
def generateRandom(**kargs):
    result = list()
    num = kargs["num"]
    struct = kargs["struct"]
    for i in range(num):
        element = list()
        for key, val in struct.items():
            if key == "int":
                it = iter(val["range"])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(val["range"])
                element.append(random.uniform(next(it), next(it)))
            elif key =="str":
                strRange = val["range"]
                strLength = val["length"]
                string = ""
                for j in range(strLength):
                    string+=random.choice(strRange)
                element.append(string)
            elif key == "bool":
                for ith in range(val["num"]):
                    element.append(random.choice((True, False)))
            else:
                element.append("未知类型")
        result.append(element)
    return result


argument = {"num": 10000, "struct": {"bool": {"num": 2}}}
resultList = generateRandom(**argument)