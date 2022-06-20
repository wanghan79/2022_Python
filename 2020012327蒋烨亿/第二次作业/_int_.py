from funcs import functions as Funcs

def readfile(file):
    list = []
    with open(file) as a:
        for line in a:
            list.append(line.strip())
    a.close()
    return list

funcsnames = readfile("name.txt")

def callPackageFunc(funcName:str):
    print(eval(funcName))

for funcsname in funcsnames:
    callPackageFunc(funcsname)
