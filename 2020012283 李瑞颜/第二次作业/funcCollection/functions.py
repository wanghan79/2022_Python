"""
    @Author  : Ruiyan Li
    @File    : functions
    @Software: PyCharm
    @Describe: 编写一个Python包，包里提供若干函数，再写一个py文件，通过读取文本文件中指定的函数名，能够调用该包中的函数。
"""


def funcA():
    print("This is funcA")


def funcB():
    print("This is funcB")


def funcC():
    print("This is funcC")


def funcD():
    print("This is funcD")




# funcDict = {"a": funcA, "b": funcB, 'c': funcC, 'd': funcD, 'e': txtFileReader}
#
#
# def callFunc(action, *args):
#     funcDict[action](args)
