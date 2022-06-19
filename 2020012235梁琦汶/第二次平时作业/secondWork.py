"""
 Author:CreamCheese
 purpose:pass
 created:2022/6/20 00:00
"""
import funcsPack.funcs as funcs
def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

#  STEP1: reading a config txt file,obtaining function name
funcsname = txtFileReader("funclist.txt")

#  STEP2: define a function to call the functions in the package
def callOutsideFunc(funcName:str):
    print(eval(funcName))

def callOutsideFunc(funcNames):
    for func in funcNames:
        print(eval(func))
#  STEP3: test the function defined in STEP2
callOutsideFunc(funcsname)