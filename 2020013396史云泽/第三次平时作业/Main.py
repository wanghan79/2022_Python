import random

import decorator.ACC as ACC
import decorator.MCC as MCC

@ACC.Decorator
def pred1():
    # struct1 = [(1, 1), (1, 0), (0, 1), (0, 0)]
    struct2 = []
    for i in range(100):
        struct2.append((bool(random.getrandbits(1)),
                        bool(random.getrandbits(1))))
    return struct2

@MCC.Decorator
@ACC.Decorator
@ACC.Decorator
def pred2():
    struct2 = []
    for i in range(100):
        struct2.append((bool(random.getrandbits(1)),
                        bool(random.getrandbits(1))))
    return struct2

#模拟二分类预测结果
pred1()
#马修相关系数
pred2()
