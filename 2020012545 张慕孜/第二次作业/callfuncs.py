#第一种
# import secondwork.funcs as funcs
#
# funcs.funcA()

#第二种
import secondwork.funcs as funcs

def txtReader(file):
    files = []
    with open(file) as f:
        for item in f:
            files.append(item)
    f.close()
    return files

funcsname = txtReader("funclist.txt")

def callFuncs(funcsName:str):
    print(eval(funcsName))

for i in funcsname:
    callFuncs(i)