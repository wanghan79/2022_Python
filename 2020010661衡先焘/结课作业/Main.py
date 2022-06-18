"""
   Author: hxt
   Created: 2022/5/26
"""
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


"""
这里不要对一个函数进行两个修饰器修饰。
yield返回的对象遍历完就没了，想要从新获取遍历头节点，就只有从新来遍历。
所以，像同时做ACC和MCC应该把代码写在一起，这样可以减少一次遍历，提高运行效率
"""


@CC.Decorator
def cc(num, struct):
    for e in GenerateRandom2(num, **struct):
        yield e[0]


if __name__ == '__main__':
    cin = generateStruct(path="data/test.txt")
    acc(4, cin)
    mcc(2, cin)
    cc(2, cin)
