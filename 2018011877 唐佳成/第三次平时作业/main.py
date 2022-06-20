# 平时作业三：实现2个修饰器ACC和MCC，对模拟二分类预测结果的精度和马修相关系数进行计算，其中模拟预测结果采用随机数生成函数作为被修饰函数

from deco import ACC, MCC
import random

def gen_bool() -> bool:
    return random.randint(0, 1) == 1

def gen_data(n: int) -> list[tuple[bool, bool]]:
    res: list[tuple[bool, bool]] = []
    for i in range(0, n):
        res.append(( gen_bool(), gen_bool()))
    return res

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
