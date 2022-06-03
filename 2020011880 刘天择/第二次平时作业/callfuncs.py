import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

funcsname = txtFileReader("funclist.txt")

def callOutsideFunc(funcName: str):
    eval(funcName)

callOutsideFunc(funcsname.pop())

