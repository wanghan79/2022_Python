"""
    @Author  : Ruiyan Li
    @File    : do.py
    @Software: PyCharm
    @Describe: 编写一个Python包，包里提供若干函数，再写一个py文件，通过读取文本文件中指定的函数名，能够调用该包中的函数。
"""
import funcCollection.functions as func


def txtFileReader(file):
    funcslist = []
    with open(file) as f:
        funcslist = f.read().splitlines()
    f.close()
    # print(funcslist)
    return funcslist


def callBackFunc(funcList):
    for _ in funcList:
        eval('func.'+_)


flist = txtFileReader('config.txt')
callBackFunc(flist)


