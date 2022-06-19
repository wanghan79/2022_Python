import funlib.funcs as funcs
def txtFileReader(file):
    lstfiles=[]
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

# STEP1: read a config text file,obtaining function name
funcsname = txtFileReader("funclist.txt")
# STEP2: define a function to call functions in the package
def callOutSideFunc(funcName):
    print(eval(funcName))
# STEP3: text the function define in STEP2
callOutSideFunc(funcsname.pop())
