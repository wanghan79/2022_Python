import functions.funs as fc


def textFileReader(file):
    listfile = []
    with open(file) as f:
        for line in f:
            listfile.append(line)
    f.close()
    return listfile


funcsname = textFileReader("functions.txt")


def callFuns(func):
    eval(func)


for item in funcsname:
    callFuns(item)
