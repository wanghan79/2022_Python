from funcs import functions as Funcs

def readfile(file):
    list = []
    with open(file) as f:
        for line in f:
            list.append(line.strip())
    f.close()
    return list

funcsnames = readfile("name.txt")

def callPackageFunc(funcName:str):
    print(eval(funcName))

for funcsname in funcsnames:
    callPackageFunc(funcsname)
