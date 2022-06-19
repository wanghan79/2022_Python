import random
import math


class Decorator:
    def __init__(self, static):
        self.__static = static

    def __call__(self, func):
        if func is None:
            return None
        if self.__static == "ACC":
            return self.ACC(func)
        elif self.__static == "MCC":
            return self.MCC(func)

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
    for index in range(0, num):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                for i in range(0, value["num"]):
                    it = iter(value['datarange'])
                    element.append(random.randint(next(it), next(it)))
            else:
                break
        yield element


struct = {"num": 10000, "struct": {"int": {"num": 2, "datarange": (0, 1)}}}

res = structDataSampling(**struct)
print(res)
