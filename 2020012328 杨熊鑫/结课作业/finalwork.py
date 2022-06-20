import math
import time
import random
import tracemalloc


class ResultAnalysis:
    def __init__(self, func):
        self.__func = func

    def __call__(self, **kwargs):
        results = self.__func(**kwargs)
        if results is None:
            return None
        else:
            statistic = self.statisticResult(results)
            print("The accuracy ACC = %f" % self.ACC(statistic))
            print("The matthews correlation coefficient MCC = %f" % self.MCC(statistic))

    def statisticResult(self, data):
        TP = TN = FP = FN = 0
        for item in data:
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
        return [TP, TN, FP, FN]

    def ACC(self, statistic):
        TP, TN, FP, FN = statistic
        acc = (TP + TN) / (TP + TN + FP + FN)
        return acc

    def MCC(self, statistic):
        TP, TN, FP, FN = statistic
        denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        if denominator != 0:
            mcc = (TP * TN - FP * FN) / denominator
        else:
            mcc = 0
        return mcc


@ResultAnalysis
# Different from homework3.
# Here, we use the generator.
def generateRandomBooleanData(**kwargs):
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "bool":
                for i in range(value["cnt"]):
                    tmp = random.choice((True, False))
                    element.append(tmp)
            else:
                print("wrong data type")
                break
        yield element


if __name__ == "__main__":
    tracemalloc.start()

    randomBooleanData = {"num": int(input("Please enter an integer : ")), "struct": {"bool": {"cnt": 2}}}

    start_time = time.time()

    generateRandomBooleanData(**randomBooleanData)

    end_time = time.time()

    usage, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"The running time of the process is: {end_time - start_time} s")
    print(f"Current memory usage is {usage / 10 ** 6}MB; Peak is {peak / 10 ** 6}MB")
