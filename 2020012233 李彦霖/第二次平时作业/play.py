import func.funcs as funcs

func = funcs.txtFileReader("liyanlin2.txt")

def txtFileReader(file):
    listfiles = []
    with open(file) as f:
        for line in f:
            listfiles.append(line)
    f.close()
    return listfiles

def callOutsideFunc(funcName: str):
    eval(funcName)


callOutsideFunc(func.pop())
