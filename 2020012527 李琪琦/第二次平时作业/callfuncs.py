import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

#   STEP1: read a config txt file, obtaining function name(在文本文件中取出函数名)
funcsname = txtFileReader("funclist.txt")

#   STEP2: define a function to call the functions in the package(通过函数封装取出，将取出的转换为代码)
def callPackageFunc(funcNames):
    for func in funcNames:
        eval(func)  #运行txt文件中的所有
    #print(eval(funcName))：仅能运行txt文件中的头一个且具有返回值none


#   STEP3: test the function defined in STEP2(实现调用)
callPackageFunc(funcsname)