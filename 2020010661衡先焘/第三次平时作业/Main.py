"""
   Author: hxt
   Created: 2022/5/26 
"""
import random

import decorator.ACC as ACC
import decorator.MCC as MCC

print("===第三次平时作业===")
# accuracy 准确率的求值 https://www.jianshu.com/p/8b7324b0f307
@ACC.Decorator
def pred1():
    # struct1 = [(1, 1), (1, 0), (0, 1), (0, 0)]
    struct2 = []
    for i in range(1000):
        struct2.append((bool(random.getrandbits(1)),
                        bool(random.getrandbits(1))))
    return struct2


# 马修斯相关系数求解 https://blog.csdn.net/YW_Vine/article/details/120779712
@MCC.Decorator
@ACC.Decorator
@ACC.Decorator  # 可以连续多次修饰
def pred2():
    struct2 = []
    for i in range(1000):
        struct2.append((bool(random.getrandbits(1)),
                        bool(random.getrandbits(1))))
    return struct2


pred1()
pred2()
