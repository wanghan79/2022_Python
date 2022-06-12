import funcspackage.functions as funcs

def readfile(file):
    list = []
    with open(file) as f:
        for line in f:
            list.append(line.strip()) #去除首尾的空格和回车
    f.close()
    return list

funcsnames = readfile("filelist.txt")

def callPackageFunc(funcName:str):
    print(eval(funcName))

for funcsname in funcsnames:
    callPackageFunc(funcsname)
