import numpy as np
from functools import wraps
from math import sqrt
b=np.array([1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1])  # 二分类的结果用 0 1 表示

def generate_random_list(n):
    for i in range(n):
        exp_list= np.random.randint(0,2,20)
        a_list = exp_list
        a_list = np.array(a_list, dtype=bool)  # 转化成布尔型,便于取反
        b_list = np.array(b, dtype=bool)
        tp_list = ((a_list) & (b_list))
        fp_list = ((a_list) & (~b_list))
        tn_list = ((~a_list) & (~b_list))
        fn_list = ((~a_list) & (b_list))
        tp = np.sum(tp_list == 1)  # 求出tp,tn,fp,fn
        fp = np.sum(fp_list == 1)
        tn = np.sum(tn_list == 1)
        fn = np.sum(fn_list == 1)
        print(exp_list)   # 预测的二分类结果
        print(b)          # 实际的二分类结果
        numerator = (tp * tn) - (fp * fn)  # 马修斯相关系数公式分子部分
        denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))  # 马修斯相关系数公式分母部分
        mcc = numerator / denominator
        acc = (tp + tn) / (tp + tn + fp + fn)
        print("精度accuracy   为 " + str(acc))
        print("马修斯相关系数mcc为 " + str(mcc))
        yield i


if __name__ == '__main__':
    o = generate_random_list(10)
    print(next(o))
    print(next(o))
    print(next(o))


