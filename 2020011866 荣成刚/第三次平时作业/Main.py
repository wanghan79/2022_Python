import random

from ResultAnalysis.Decorator import ACC, MCC


@ACC.DecoratorAcc
def predictACC(num):
    list = []
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(num):
        list.append((bool(random.getrandbits(1)), bool(random.getrandbits(1))))

    for i in list:
        if i[0] & i[1]:
            tp += 1
        elif (~ i[0]) & i[1]:
            fp += 1
        elif i[0] & ~i[1]:
            fn += 1
        else:
            tn += 1
    struct = (tp, tn, fp, fn)
    print("总样本数为: ", (tp + tn + fp + fn))
    return struct


@MCC.DecoratorMcc
def predictMcc(num):
    list = []
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(num):
        list.append((bool(random.getrandbits(1)), bool(random.getrandbits(1))))

    for i in list:
        if i[0] & i[1]:
            tp += 1
        elif (~ i[0]) & i[1]:
            fp += 1
        elif i[0] & ~i[1]:
            fn += 1
        else:
            tn += 1
    struct = (tp, tn, fp, fn)
    print("总样本数为: ", (tp + tn + fp + fn))
    return struct


predictACC(10000)
predictMcc(10000)
