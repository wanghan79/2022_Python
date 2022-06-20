import random
import math

def ACC(self, func):
        def wrapper(num, **kwargs):
            result = func(num, **kwargs)
            cnt = 0
            for i in range(0, num):
                if result[i][0] == result[i][1]:
                    cnt += 1
            acc = cnt / num
            print("ACC : %f" % acc)
            return result

        return wrapper

def MCC(self, func):
        def wrapper(num, **kwargs):
            result = func(num, **kwargs)
            TP = FN = FP = TN = 0
            for i in range(0, num):
                if result[i][0] == 1 and result[i][1] == 1:
                    TP += 1
                elif result[i][0] == 1 and result[i][1] == 0:
                    FN += 1
                elif result[i][0] == 0 and result[i][1] == 1:
                    FP += 1
                elif result[i][0] == 0 and result[i][1] == 0:
                    TN += 1
            mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
            print("MCC : %f" % mcc)
            return result

        return wrapper
    
@Decorator("MCC")
@Decorator("ACC")
def structDataSampling(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "bool":
                for i in range(0, value["num"]):
                    t = iter(value['datarange'])
                    element.append(random.randint(next(t), next(t)))
            else:
                break
        result.append(element)
    return result

struct = {"num": 10000, "struct": {"bool": {"num": 2, "datarange": (0, 1)}}}

list = structDataSampling(**struct)
print(list)
