import math
import random
from functools import wraps

#函数修饰器
def decWith(flag): #flag可以是ACC或者MCC
    def dector(func): #定义ACC以及MCC修饰器
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs) #调用随机数生成函数，在这里是func()，调用之后会生成一个列表
            #acc和mcc
            total = len(result)
            TP = TN = FP = FN = 0
            for e in result: #统计false以及true个数套用公式
                if (e[0] is True) and (e[1] is True):
                    TP += 1
                elif (e[0] is True) and (e[1] is False):
                    FN += 1
                elif (e[0] is False) and (e[1] is True):
                    FP += 1
                elif (e[0] is False) and (e[1] is False):
                    TN += 1
                else:
                    pass
            if flag == "ACC": #修饰器ACC
                acc = (TP + TN) / total
                print("ACC : %f" % acc)
            elif flag == "MCC": #修饰器MCC
                mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC : %f" % mcc)
            else:
                pass
            return result
        return wrapper
    return dector


#被修饰的函数
@decWith("MCC")
@decWith("ACC")
def structDataSampling(**kwargs): #生成bool随机数，同作业1  第一个bool值是真实值，第二个bool值是预测值
    result = list()
    num = kwargs["num"] #生成个数
    struct = kwargs["struct"] #生成元素对应类型的随机数
    for item in range(num):
        element = list()
        for key, value in struct.items():
            if key == "int":
                it = iter(value["datarange"])
                element.append(random.randint(next(it), next(it)))
            # elif key == "float":
            #     it = iter(value["datarange"])
            #     element.append(random.uniform(next(it), next(it)))
            # elif key =="str":
            #     strRange = value["datarange"]
            #     strLength = value["len"]
            #     string = ""
            #     for i in range(strLength):
            #         string += random.choice(strRange)
            #     element.append(string)
            elif key == "bool":
                for j in range(value["num"]):
                    element.append(random.choice((True, False))) #bool类型范围从true以及false中选择
            else:
                break
        result.append(element)
    return result #生成一个列表

para = {"num": 10000, "struct": {"bool": {"num":2}}}

resultL = structDataSampling(**para)
# print(resultL)