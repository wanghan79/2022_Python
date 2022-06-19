import random
from functools import wraps
import math


#flag can be ACC or MCC
def decorateWith(flag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            total = len(result)
            TP = TN = FP = FN = 0
            for e in result:
                if (e[0] is True) and (e[1] is True):
                    TP += 1
                elif (e[0] is True) and (e[1] is False):
                    TN += 1
                elif (e[0] is False) and (e[1] is True):
                    FP += 1
                elif (e[0] is False) and (e[1] is False):
                    FN += 1
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
    return decorator


@decorateWith("MCC")
@decorateWith("ACC")
def structDataSampling(**kwargs):
    """
    :param num:生成元组个数
    :param kwargs:传入的字典
    :return:各元组里True or False的详细次数
    """
    num = kwargs["num"]
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "bool":
                number = value['num']
                for i in range(0, number):
                    tmp = random.choice((True, False))
                    element.append(tmp)
            else:
                break
        result.append(element)
    return result


def main():
    text = open("decorater.txt")
    struct = eval(text.read())
    result = structDataSampling(**struct)

    for item in result:
        print(item)


if __name__ == '__main__':

    main()
