import funcsPackage.functions.funcs as funcs

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

funcsname = txtFileReader("functionlist.txt")


def callPackageFunc(funcName):
    for func in funcName:
        print(eval(func))


callPackageFunc(funcsname)
