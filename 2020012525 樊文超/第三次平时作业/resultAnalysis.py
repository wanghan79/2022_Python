import math
import random
import tracemalloc
from functools import wraps

'''
    平时作业三：实现2个修饰器ACC和MCC，对模拟二分类预测结果的精度和马修相关系数进行计算，
    其中模拟预测结果采用随机数生成函数作为被修饰函数
'''
# TP：真阳性；TN：真阴性；FP：假阳性；FN：假阴性
TP = TN = FP = FN = 0

def binaInit():
    def caculation(func):
        @wraps(func)
        def wrapper(*arg, **kwargs):
            dataList = func(*arg, **kwargs)
            global TP, TN, FP, FN
            for data in dataList:
                if data[0]:
                    if data[1]:
                        TP += 1
                    else:
                        FP += 1
                else:
                    if data[1]:
                        FN += 1
                    else:
                        TN += 1
            return dataList
        return wrapper
    return caculation

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
            print("MCC : {:.2%}".format((TP * TN - FP * FN) / math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))))
            return dataList
        return wrapper
    return calculation


@ACC()
@MCC()
@binaInit()
def randomBoolGenerator(**struct):
    result = list()
    for item in range(0, struct['num']):
        element = list()
        # 对每个参数列表的每个键值对
        for key, value in struct.items():
            if key == 'num':
                continue
            elif key == 'bool':
                for ith in range(value):
                    tmp = random.choice((True, False))
                    element.append(tmp)
            else:
                print("数据类型不支持")
                continue
        result.append(element)
    return result

if __name__ == '__main__':
    # 内存检测
    dataStruct = {"num": 10000, "bool": 2}
    tracemalloc.start()
    resultList = randomBoolGenerator(**dataStruct)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
