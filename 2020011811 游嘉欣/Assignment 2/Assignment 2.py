import myfuncs.func as func

def txtFileReader(file):
    lstfiles=[]
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles
funcsname =  txtFileReader("funcList.txt")
def callPackageFunc(funcname:str):
    for fun in funcname:
        eval(fun)

callPackageFunc(funcsname)