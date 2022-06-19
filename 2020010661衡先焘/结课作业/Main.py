"""
   Author: hxt
   Created: 2022/5/26
"""
import tracemalloc

import decorator.ACC as ACC
import decorator.MCC as MCC
import decorator.CC as CC

from util.RandomDataUtil import GenerateRandom2, generateStruct


@ACC.Decorator
def acc(num, struct):
    for e in GenerateRandom2(num, **struct):
        yield e[0]


@MCC.Decorator
def mcc(num, struct):
    for e in GenerateRandom2(num, **struct):
        yield e[0]  # e是随机数组，例如[1, 10.2, "aav", [(1, 0),(1, 1)]] 这里要用元组那个数据


@CC.Decorator
def cc(num, struct):
    for e in GenerateRandom2(num, **struct):
        yield e[0]


"""
这里不要对一个函数进行两个修饰器修饰。
yield返回的对象遍历完就没了，想要从新获取遍历头节点，就只有从新来遍历。
所以，像同时做ACC和MCC应该把代码写在一起，这样可以减少一次遍历，提高运行效率.

@MCC.Decorator
def getRandoms(**kwargs):
    generator = Random(**kwargs)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList
    
像上面这种方式，我个人认为是不妥善的，yield的目的就是为了减少内存消耗，
而这样还是去把迭代的东西加在一起，扩大了内存的使用，违背了使用yield的初衷！

下面我还对此做了一点点粗略的对比
"""


@ACC.OldDecorator
def dd(num, struct):
    l = list()
    for e in GenerateRandom2(num, **struct):
        l.append(e[0])
    return l[0]


if __name__ == '__main__':
    tracemalloc.start()
    cin = generateStruct(path="data/test.txt")
    acc(10, cin)
    mcc(2, cin)
    # cc(2, cin)
    # dd(10, cin)  # 用去对比的
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("Current memory usage is {:.3}MB; Peak was {:.3}MB".
          format(current / 10 ** 6, peak / 10 ** 6))

"""
对比结果:
前提【元组数组有10000个(0, 0)】
当有10批这样的数据时：
yield方式 --> Current memory usage is 0.110128MB; Peak was 0.197708MB
return方式 --> Current memory usage is 0.108544MB; Peak was 0.896584MB

当有20批这样的数据时：
yield方式 --> Current memory usage is 0.112048MB; Peak was 0.199628MB
return方式 --> Current memory usage is 0.109824MB; Peak was 1.773536MB


不难看出yield方式提高了使用的上限，内存峰值几乎保持不变。
而直接append上所有的数据，会导致内存峰值急剧上升。
"""
