# 结课大作业：改写平时作业三，采用生成器方式生成相应随机数

from deco import ACC, MCC
import random

def gen_bool() -> bool:
    return random.randint(0, 1) == 1

def gen_data(n: int):
    for i in range(0, n):
        yield ( gen_bool(), gen_bool())
    return

@ACC
def acc_binder(n: int):
    return gen_data(n)

@MCC
def mcc_binder(n: int):
    return gen_data(n)

n = 100

print('n = %d' % n)
print('ACC = %f' % acc_binder(n))
print('MCC = %f' % mcc_binder(n))
