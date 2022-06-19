import random
from math import sqrt
from functools import wraps

"""
 Author:Ren
"""

class decorator:
    def __init__(self, static="ACC"):
        self.__static = static

    def __call__(self, func, *args, **kwargs):
        @wraps(func)
        def wrapper(**kwargs):
            results = func(**kwargs)
            if results is None:
                return None
            if self.__static == "ACC":
                self.ACC(results)
            elif self.__static == "MCC":
                self.MCC(results)
            return results

        return wrapper

    def ACC(self, results):
        n = len(results)
        count = 0
        for i in range(n):
            if results[i][0] == results[i][1]:
                count += 1
        acc = count / n
        print("ACC = {}".format(acc))

    def MCC(self, results):
        TP, FP, TN, FN = 0, 0, 0, 0
        for i in results:
            if (i[0] is True) and (i[1] is True):
                TP += 1
            elif (i[0] is True) and (i[1] is False):
                FN += 1
            elif (i[0] is False) and (i[1] is True):
                FP += 1
            elif (i[0] is False) and (i[1] is False):
                TN += 1
            else:
                pass
        mcc = ((TP * TN) - (FP * FN)) / sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        print("MCC = {}".format(mcc))


# Step2 A random number generating function is constructed and decorated with ACC and MCC
class RandomA:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for i in range(self.num):
            if i == self.num:
                raise StopIteration
            element = list()
            for key, value in self.struct.items():
                if key == "int":
                    it = iter(value['datarange'])
                    element.append(random.randint(next(it), next(it)))
                elif key == "float":
                    it = iter(value['datarange'])
                    element.append(random.uniform(next(it), next(it)))
                elif key == "str":
                    element.append(
                        ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen'])))
                elif key == "bool":
                    for ith in range(value["number"]):
                        element.append(random.choice((True, False)))
                else:
                    break
            yield element


@decorator("MCC")
@decorator("ACC")
def RandomB(**kwargs):
    generator = RandomA(**kwargs)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList


para = {"num": 10000, "struct": {"bool": {"number": 2}}}
RandomB(**para)

# if __name__ == '__main__':
#     para = {'num': 1000, 'struct': {'bool': {"number": 2}}}
#     format(structDataSampling(**para))
