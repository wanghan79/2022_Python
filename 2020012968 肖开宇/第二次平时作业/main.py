# @Time        : 2022/6/15 19:30
# @Author      : 2020012968 肖开宇
# @File        : main.py
# @Description : 第二次平时作业


import funcsPack.funcs as funcs


# 通过读取文本文件中指定的函数名调用该包中的函数

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles


# STEP1: read a config txt file, obtaining function name
funcsname = txtFileReader("funclist.txt")


# STEP2: define a function to call the functions in the package
def callPackageFunc(funcName):
    for funcname in funcName:
        eval(funcname)


# STEP3: test the function defined in STEP2
callPackageFunc(funcsname)
