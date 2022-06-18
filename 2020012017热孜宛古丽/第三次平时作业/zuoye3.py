import math
import random
from functools import wraps



def decorateWith(flag):
    def decorator(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)  #total是Accuracy中正确的预测结果的数量
            tp = tn = fp = fn = 0
            for item in result:
                if (item[0] is True)&(item[1] is True):
                    tp=tp+1  #预测对，预测结果为正
                elif (item[0] is True)&(item[1] is False):
                    fn= fn+1  #预测错，预测结果为负
                elif (item[0] is False)&(item[1] is True):
                    fp=fp+1   #预测错，预测结果为正
                elif (item[0] is False) & (item[1] is False):
                    tn=tn+1   #预测对，预测结果为负
                else:
                    pass
            if flag == "ACC":   #准确度
                acc = (tp + tn) / total
                print("ACC : %f" %acc)
            elif flag == "MCC":  #马修斯相关系数
                t = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
                mcc = (tp * tn - fp * fn) / t
                print("MCC : %f" %mcc)
            else:
                pass
            return result
        return wrapper
    return decorator

@decorateWith("MCC")
@decorateWith("ACC")
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
                element.append(" ")
        result.append(element)
    return result


argument = {"num": 10000, "struct": {"bool": {"num": 2}}}
resultList = generateRandom(**argument)
