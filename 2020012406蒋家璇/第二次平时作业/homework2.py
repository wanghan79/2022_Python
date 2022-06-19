""" 
    @Time    : 2022/6/10 11:05
    @Author  : Jiaxuan Jiang
    @Email   : 6812624@qq.com
    @File    : homework2.py
    @Software: PyCharm
"""
import funcsPack.funcs as funcs


def txtFileReader(file):
    lstFiles = []
    with open(file) as f:
        for line in f:
            lstFiles.append(line)
    f.close()
    return lstFiles


# STEP1 read a txt file, obtaining function name
funcsName = txtFileReader("funcList.txt")


# STEP2 call the functions in the package(funcsPack)
def callOutsideFunc(funcName: str):
    eval(funcName)  # eval()函数用于执行一个字符串表达式,并且返回该表达式的值,这里返回的是函数表达式的值


# STEP3 call the function in STEP2
for i in range(len(funcsName)):
    callOutsideFunc(funcsName[i])
