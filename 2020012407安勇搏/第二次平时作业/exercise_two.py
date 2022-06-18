#exercise two
import functions.func as fc

def textFileReader(file):
    lstfile = []
    with open(file) as f:
        for line in f:
            lstfile.append(line)
        f.close()
        return lstfile

funcname = textFileReader("functions.txt")

def callPakageFunc(funcname):
    for funs in funcname:
        eval(funs)

callPakageFunc(funcname)
