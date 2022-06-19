# coding=utf-8
from newPkg.function import *

def read_text(filePath):
    with open(filePath, 'r') as fp:
        lstRead = fp.readlines()
        lstRtn = [x.replace("\n","") for x in lstRead]
    return lstRtn


filePath = input('输入路径:')
lstFunc = read_text(filePath)

for fun in lstFunc:
    exec(fun+"()",globals())