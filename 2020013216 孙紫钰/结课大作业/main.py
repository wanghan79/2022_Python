import math
import random
from functools import wraps

def decWith(flag): #flag可以是ACC或者MCC
#同作业3
    def dector(func): #定义ACC以及MCC修饰器
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs) #调用随机数生成函数，在这里是func()，调用之后会生成一个列表
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

#采用生成器方法生成随机数
class Random:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self): #调用next时调用
        for i in range(self.num):
            if i == self.num:
                raise StopIteration
            element = list()
            for key, val in self.struct.items():
                if key == "int":
                    it = iter(val["datarange"])
                    element.append(random.randint(next(it), next(it)))
                # elif key == "float":
                #     it = iter(val["datarange"])
                #     element.append(random.uniform(next(it), next(it)))
                # elif key =="str":
                #     strRange = val["datarange"]
                #     strLength = val["len"]
                #     string = ""
                #     for i in range(strLength):
                #         string+=random.choice(strRange)
                #     element.append(string)
                elif key == "bool":
                    for j in range(val["num"]):
                        element.append(random.choice((True, False))) #bool类型范围从true以及false中选择
                else:
                    break
            yield element #用yield返回，可以记录位置


@decWith("MCC")
@decWith("ACC")
def structDataSampling(**kwargs):
    generator = Random(**kwargs)
    resultL = []
    for element in generator:
        resultL.append(element)
    return resultL



para = {"num": 5,"struct": {"bool": {"num":2}}}

resultL = structDataSampling(**para)
# for elem in resultL:
#     print(elem)