import funcsPack.funcs as funcs


def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
        f.close()
        return lstfiles

#STEP1:read a config txt file,obtaining function name
funcsname = txtFileReader("funclist.txt")


#STEP2:define a function to call the functions in the package
def callPackageFunc(funcName: str):
    eval(funcName)


#STEP3:test the function defined in STEP2
callPackageFunc(funcsname.pop())





