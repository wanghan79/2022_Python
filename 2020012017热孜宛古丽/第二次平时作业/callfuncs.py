import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfiles=[]
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles
funcsname=txtFileReader("funclist.txt")

def callPackageFunc(funcName:str):
    eval(funcName)
callPackageFunc("funcs.funcB()")

# print(eval(funcName))
# callPackageFunc(funcsname.pop())


