
import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

# STEP1: read a config txt file, obtaining function name
funcsname = txtFileReader("func_list.txt")

# STEP2: define a function to call the functions in the package
def callPackageFunc(funcNames):
    for func in funcNames:
        eval(func)

# STEP3: test the function in STEP2
callPackageFunc(funcsname)

