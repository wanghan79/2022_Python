import random


class ResultAnalysis:
    def __init__(self, func="ACC"):
        self.__func = func
        # self.__static = static

    def __call__(self, f):
        def wrap(*args, **kwargs):
            result = f(*args, **kwargs)
            eval('self.' + self.__func)(result)
            return result

        return wrap

    def ACC(self, data):
        # print(data)
        # data: [(predict, real)]
        TP = data.count((True, True))
        TN = data.count((False, False))
        Acc = (TP + TN) / len(data)
        print("Accuracy: {:.2}".format(Acc))

    def MCC(self, data):
        TP = data.count((True, True))
        FP = data.count((False, True))
        TN = data.count((False, False))
        FN = data.count((True, False))
        N = TN + TP + FN + FP
        S = (TP + FN) / N
        P = (TP + FP) / N
        Mcc = 0
        if P * S * (1 - S) * (1 - P) != 0:
            Mcc = (TP / N - S * P) / (P * S * (1 - S) * (1 - P))
        print("Matthews correlation coefficient: {:.2}".format(Mcc))


def structDataSampling(num, **struct):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in struct.items():
            if key == "bool":
                tmp = tuple([random.choice([True, False]) for _ in range(value['len'])])
            else:
                break
            element = tmp
            yield tmp
        # result.append(element)
    # return result


@ResultAnalysis('ACC')
def test1():
    print('#Test 1:')
    dataGenerator = structDataSampling(500, bool={'len': 2})
    data = []
    for i in dataGenerator:
        data.append(i)
    return data


@ResultAnalysis('MCC')
@ResultAnalysis('MCC')
@ResultAnalysis('ACC')
def test2():
    print('#Test 2:')
    dataGenerator = structDataSampling(50000, bool={'len': 2})
    data = []
    for i in dataGenerator:
        data.append(i)
    return data


# data: [(predict, real)]


test1()
test2()
