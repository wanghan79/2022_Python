import Funcs_package.functions as funcs
import string

"""
作业要求：
编写一个Python包，包里提供若干函数，再写一个py文件，通过读取文本文件中指定的函数名，能够调用该包中的函数。
"""


def fileRead(file):
    lines = []
    with open(file, 'r') as f:
        for line in f:
            lines.append(line)
    return lines


if __name__ == '__main__':
    Funcs = fileRead("func_list.txt")
    for func in Funcs:
        eval("funcs." + func)()
