'''

'''
import pacaFuncs.funcs as funcs
def txtFileReader(file):
    lstfiles = []
    with  open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles





# step1: read a config txt file,obtaining function name
funcname = txtFileReader("funclist.txt")


# step2: define a function to call the function in the pacage
def callPacageFunc(funcName: str):
    eval(funcName)


# step3: test the function defined in step2
for i in funcname:
    callPacageFunc(funcname.pop())