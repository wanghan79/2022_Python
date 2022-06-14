# coding=utf-8

from newPkg.function import *


# fileReader

def fileReader(filePath):
    with open(filePath, 'r') as fp:
        lstRead = fp.readlines()
        lstRtn = []
        for item in lstRead:
            lstRtn.append(item.strip('\n'))
    return lstRtn


filePath = input('Input Path Here:')
lstFunc = fileReader(filePath)

for fun in lstFunc:
    exec(fun+"()",globals())
