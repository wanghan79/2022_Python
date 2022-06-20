import math
import time
import random
import tracemalloc
from functools import wraps


# flag can be ACC or MCC
# when flag is ACC, the function will return the accuracy
# when flag is ACC, the function will return the matthews correlation coefficient
def decorateWith(flag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            point = func(*args, **kwargs)
            TP = TN = FP = FN = 0
            for item in point:
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
                acc = (TP + TN) / (TP + TN + FP + FN)
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
            return point

        return wrapper

    return decorator


@decorateWith("MCC")
@decorateWith("ACC")
# A simplified version of generateRandomData in homework1.
# Here, we only focus on the boolean data.
def generateRandomBooleanData(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        for key, value in kwargs['struct'].items():
            if key == "bool":
                tmp = []
                for i in range(value["cnt"]):
                    tmp.append(random.choice((True, False)))
                tmp = tuple(tmp)
            else:
                tmp = "wrong data type"
        result.append(tmp)
    return result


if __name__ == "__main__":
    tracemalloc.start()  # Track memory allocation

    randomBooleanData = {"num": int(input("Please enter an integer : ")), "struct": {"bool": {"cnt": 2}}}

    start_time = time.time()  # Record running time

    generateRandomBooleanData(**randomBooleanData)

    end_time = time.time()

    usage, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"The running time of the process is: {end_time - start_time} s")
    print(f"Current memory usage is {usage / 10 ** 6}MB; Peak is {peak / 10 ** 6}MB")
