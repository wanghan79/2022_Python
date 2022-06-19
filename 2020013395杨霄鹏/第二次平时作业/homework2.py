import string
from function import *

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

funcsname = txtFileReader("funclist.txt")

def callPackageFunc(funcName: str):
    eval(funcName)

callPackageFunc(funcsname.pop())
callPackageFunc(funcsname.pop())
callPackageFunc(funcsname.pop())
