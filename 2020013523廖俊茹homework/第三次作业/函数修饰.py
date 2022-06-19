import random
import math

def decorated(flag):
    def dec(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = TN = FP = FN = 0
            for e in result:
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
            if flag == "ACC":
                acc = (TP + TN) / total
                print("ACC : %f" % acc)
            elif flag == "MCC":
                denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                mcc = (TP * TN - FP * FN) / denominator
                print("MCC : %f" % mcc)
            else:
                pass
            return result
        return wrapper
    return dec

@decorated("MCC")
@decorated("ACC")
def structDataSampling(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == 'int':
                it = iter(value['datarange'])
                element.append(random.randint(next(it), next(it)))
            elif key == 'float':
                it = iter(value['datarange'])
                element.append(random.uniform(next(it), next(it)))
            elif key == 'str':
                element.append(''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len'])))
            elif key == 'bool':
                for m in range(value['datarange']):
                    element.append(random.choice((True, False)))
            else:
                break

        result.append(element)
    return result

struct = {'bool':{'datarange':2}}
resultList = structDataSampling(10000,**struct)