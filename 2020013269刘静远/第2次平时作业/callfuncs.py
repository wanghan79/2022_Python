import funcspack.funcs as funcs
def txtfilereader(file):
    lstfiles=[]
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

funcsname = txtfilereader('text.txt')

def callpackagefunc(funcname: str):
    eval(funcname)
    #print(eval(funcname)) #使用前记得改funcs里的return的注释

callpackagefunc(funcsname.pop())