import math
import random
from functools import wraps


# flag can be ACC or MCC
# when flag is ACC, the function will return the accuracy
# when flag is ACC, the function will return the matthews correlation coefficient
def decorateWith(flag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            TP = TN = FP = FN = 0
            for item in result:
                if (item[0] is True) and (item[1] is True):
                    TP += 1
                elif (item[0] is True) and (item[1] is False):
                    FN += 1
                elif (item[0] is False) and (item[1] is True):
                    FP += 1
                elif (item[0] is False) and (item[1] is False):
                    TN += 1
                else:
                    pass
            if flag == "ACC":
                acc = (TP + TN) / len(result)
                print("The accuracy ACC = %f" % acc)
            elif flag == "MCC":
                denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                # when the denominator equals 0, mcc equals 0.
                if denominator == 0:
                    mcc = 0
                else:
                    mcc = (TP * TN - FP * FN) / denominator
                print("The matthews correlation coefficient MCC = %f" % mcc)
            else:
                pass
            return result

        return wrapper

    return decorator


@decorateWith("MCC")
@decorateWith("ACC")
def generateRandomBooleanData(**kwargs):
    result = list()
    for i in range(0, kwargs["num"]):
        element = list()
        for key, value in kwargs["struct"].items():
            if key == "bool":
                for ith in range(value["num"]):
                    element.append(random.choice((True, False)))
            else:
                element.append("unknown data type")
        result.append(element)
    return result


randomBooleanData = {"num": int(input("Please enter an integer : ")), "struct": {"bool": {"num": 2}}}
resultList = generateRandomBooleanData(**randomBooleanData)
