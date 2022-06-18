import funcsPack.funcs as funcs

def txtFileReader(file):
    lstfile = []
    with open(file)as f:
        for line in f:
            lstfile.append(line)
    f.close()
    return lstfile

#   STEP1: read a config txt file,obtaining function name
funcsname = txtFileReader("funclist.txt")

#   STEP2: define a function to call the functions in the package
def callPackageFunc(funcsName: str):
    eval(funcsName)

# #如果txt文件里包含多个函数名称，那么可以用for循环。代码变为
#     for i in funcsName:
#         eval(i)
# #STEP3变为
# callPackageFunc(funcsname)

#   STEP3: test the function defined in STEP2
callPackageFunc(funcsname.pop())



