import math
import random

from ResultAnalysis2.Decorator import ACC, MCC


@ACC.DecoratorAcc
def predictACC(num):
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    def __statistics__():
        for i in range(num):
            s = (bool(random.getrandbits(1)), bool(random.getrandbits(1)))
            yield s

    for s in __statistics__():
        if s[0] & s[1]:
            tp += 1
        elif (~ s[0]) & s[1]:
            fp += 1
        elif s[0] & ~s[1]:
            fn += 1
        else:
            tn += 1
    struct = (tp, tn, fp, fn)
    print("总结果数为: ", (tp + tn + fp + fn))
    return struct


@MCC.DecoratorMcc
def predictMcc(num):
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    def __statistics__():
        for i in range(num):
            s = (bool(random.getrandbits(1)), bool(random.getrandbits(1)))
            yield s

    for s in __statistics__():
        if s[0] & s[1]:
            tp += 1
        elif (~ s[0]) & s[1]:
            fp += 1
        elif s[0] & ~s[1]:
            fn += 1
        else:
            tn += 1

    struct = (tp, tn, fp, fn)
    print("总结果数为: ", (tp + tn + fp + fn))
    return struct


predictACC(10000)
predictMcc(10000)
