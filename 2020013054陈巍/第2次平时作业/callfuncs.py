import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfiles=[]
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles



# step1:read a config txt file,obtaining function name
funcsname=txtFileReader("funclist.txt")

# step2:define a function to call the functions in the package
def callPackageFunc(funcNames):
    for func in funcNames:
        eval(func)

# step3:test the function define in step2
callPackageFunc(funcsname)