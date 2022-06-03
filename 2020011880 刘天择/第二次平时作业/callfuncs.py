import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles


# STEP1
funcsname = txtFileReader("funclist.txt")


# STEP2
def callOutsideFunc(funcName: str):
    eval(funcName)


# STEP3
callOutsideFunc(funcsname.pop())

