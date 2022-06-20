import decorator.ACC as ACC
import decorator.MCC as MCC

from util.RandomDataUtil import RSD_Generator, S_Generator


@ACC.Decorator
def Acc(num, struct):
    for ds in RSD_Generator(num, **struct):
        yield ds[0]


@MCC.Decorator
def Mcc(num, struct):
    for ds in RSD_Generator(num, **struct):
        yield ds[0]


if __name__ == '__main__':
    data = S_Generator(path="data/data.txt")
    Acc(10, data)
    Mcc(10, data)
