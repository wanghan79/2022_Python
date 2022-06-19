"""
li
pass
2022 5/6
"""
import funcsPack.funcs as funcs

def txtFileReader(file):
    listfiles = []
    with open(file) as f:
        for line in f:
            listfiles.append(line)
    f.close()
    return listfiles


funcsname = txtFileReader("funcslist.txt")
print(funcsname)

def callPackageFunc(funcName: str):
    eval(funcName)


callPackageFunc(funcsname.pop())
