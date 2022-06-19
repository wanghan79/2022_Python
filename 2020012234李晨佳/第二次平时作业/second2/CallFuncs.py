import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles


def callPackageFunc(funcNames):
    for func in funcNames:
        eval(func)

def main():
    funcsname = txtFileReader("funclist.txt")
    callPackageFunc(funcsname)
    funcs.funcA()

main()