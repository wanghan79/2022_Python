import math
import random
def addLogging(sign):
    def decorator(func):
        def wrapper(*args, **kwargs):
            tmp = func(*args, **kwargs)
            TP = TN = FP = FN = 0
            for i in tmp:
                if (i[0] is True) and (i[1] is True):
                    TP = TP + 1
                elif (i[0] is True) and (i[1] is False):
                    FN = FN + 1
                elif (i[0] is False) and (i[1] is True):
                    FP = FP + 1
                elif (i[0] is False) and (i[1] is False):
                    TN = TN + 1
            if sign == "ACC":
                acc = (TP + TN) / (TP + TN + FP + FN)
                print("ACC = {}".format(acc))
            elif sign == "MCC":
                mcc = (TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                print("MCC = {}".format(mcc))
            return tmp
        return wrapper
    return decorator

@addLogging("ACC")
@addLogging("MCC")
def structDataSampling(**kwargs):
    results = list()
    for item in range(0,kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == "float":
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == "str":
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            elif key == "bool":
                for p in range(value['num']):
                    element.append(random.choice((True, False)))
            else:
                break
        results.append(element)
    return results

para = {"num": 1000, "struct": {"bool": {"num": 8}}}
structDataSampling(**para)
