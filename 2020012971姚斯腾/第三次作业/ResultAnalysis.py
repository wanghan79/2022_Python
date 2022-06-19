import math
import random
import time
import tracemalloc
from functools import wraps

'''
作业要求：
    实现2个修饰器ACC和MCC，对模拟二分类预测结果的精度和马修相关系数进行计算
    其中模拟预测结果采用随机数生成函数作为被修饰函数

实验原理：
    ACC = (TP + TN) / (TP + TN + FP + FN)
    MCC = [(TP * TN) - (FP * FN)] / sqrt[(TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)]
    TP(True Positive):样本预测值与真实值相符且均为正，即真阳性
    TN(True Negative):样本预测值与真实值相符且均为负，即真阴性
    FP(False Positive):样本预测值为正、真实值为负，即假阳性
    FN(False Negative):样本预测值为负、真实值为正，即假阴性

实验思路:
    步骤一：生成数据
    步骤二：根据数据初始化需要的参数(argsInit)
    步骤三：根据参数计算对模拟二分类预测结果的精度(ACC)和马修相关系数(MCC)
'''
# 真阳性
TP = 0
# 假阳性
FP = 0
# 假阴性
FN = 0
# 真阴性
TN = 0


# 根据二元组进行参数初始化，用于ACC和MCC的计算
def argsInit():
    def calculation(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dataList = func(*args, **kwargs)
            # 使用全局变量，便于其他函数使用（单线程应该是没有问题的），减少计算量（一次计算）
            global TN, TP, FP, FN
            for data in dataList:
                if data[0]:
                    # 真阳性
                    if data[1]:
                        TP += 1
                    # 假阳性
                    else:
                        FP += 1
                else:
                    # 假阴性
                    if data[1]:
                        FN += 1
                    # 真阴性
                    else:
                        TN += 1
            return dataList

        return wrapper

    return calculation


def ACC():
    def calculation(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dataList = func(*args, **kwargs)
            print("ACC : {:.2%}".format((TP + TN) / (TP + TN + FP + FN)))
            return dataList

        return wrapper

    return calculation


def MCC():
    def calculation(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dataList = func(*args, **kwargs)
            print("MCC : {:.2%}".format((TP * TN - TP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))))
            return dataList

        return wrapper

    return calculation


# 测试发现注解离函数最近先执行
@ACC()
@MCC()
@argsInit()
# 随机数生成，但是只保留布尔类型的随机数生成功能
def randomBoolGenerator(**struct):
    result = list()
    for item in range(0, struct['num']):
        element = list()
        # 对每个参数列表的每个键值对
        for key, value in struct.items():
            # 由于第一个键值对是数据条数，要过掉
            if key == "num":
                continue
            elif key == "bool":
                for ith in range(value):
                    tmp = random.choice((True, False))
                    element.append(tmp)
            else:
                print("数据错误")
                continue
        result.append(element)
    return result


# 使用内存监控来查看对比使用生成器前后的程序运行内存大小:
if __name__ == "__main__":
    tracemalloc.start()

    # num ：数据条目
    # bool 数据类型 ， 2 指的是二元组
    dataStruct = {"num": 10000, "bool": 2}
    myResultList = randomBoolGenerator(**dataStruct)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")

    # 打印四个参数
    # print(TP, TN, FP, FN)

'''
打印结果样例：
MCC : -0.01%
ACC : 49.92%
Current memory usage is 0.970957MB; Peak was 0.971151MB
'''
