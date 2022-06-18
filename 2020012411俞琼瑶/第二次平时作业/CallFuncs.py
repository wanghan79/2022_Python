"""
    Author: yqy
    Created: 2022/4/25 21:37
"""
import funcsPack.Funcs as Funcs


def txtFileReader(file):
    lstFiles = []
    with open(file) as f:
        for line in f:
            lstFiles.append(line)
    f.close()
    return lstFiles


# 读取config.txt
funcsName = txtFileReader("config.txt")


# 定义一个函数去调用funcsPack包里的函数
# config文件里单个方法
def callOutsideFunc(funcName: str):
    # print eval函数的返回值，如果funcA里有return，则是打印return的内容，否则就是none
    print(eval(funcName))


# 调用多个方法
def callOutsideFuncs(funcNames):
    # print eval函数的返回值，如果funcA里有return，则是打印return的内容，否则就是none
    for func in funcNames:
        print(eval(func))


# 测试
# 单个方法
callOutsideFunc(funcsName.pop())
# callOutsideFunc("Funcs.funcA()")
# 多个方法
# callOutsideFuncs(funcsName)
