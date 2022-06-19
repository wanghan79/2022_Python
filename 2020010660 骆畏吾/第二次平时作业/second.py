"""
Author:weiw
Purpose:pass.
Created:6/12
"""
import funsPack.sec_func as funcs

def obfuncs(path:str):
    with open(path, "r") as f:
        funct = f.read()
    return funct.split()

functionNames = obfuncs("funclist")

for funcName in functionNames:
    eval("funcs." + funcName)()