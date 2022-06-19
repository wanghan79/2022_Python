import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfile = []
    with open(file)as f:
        for line in f:
            lstfile.append(line)
    f.close()
    return lstfile


funcsname = txtFileReader("funclist.txt")


def callPackageFunc(funcsName: str):
    eval(funcsName)

callPackageFunc(funcsname.pop())
