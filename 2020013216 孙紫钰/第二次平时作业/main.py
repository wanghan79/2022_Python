import funcsPack.funcs as funcs

#调用函数

def txtFileReader(file): #读取给定文件的每一行
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line) #把文件中每一行拿出来，存到一个list里面并且返回
    f.close()
    return lstfiles

# 读取调用txt文件，获取函数名称
funcsname = txtFileReader("funclist.txt")

# 定义一个函数去调用包内的函数
def callPackageFunc(funcNames):
    for func in funcNames:  #循环执行多个
        eval(func)
    # eval(funcName)  #单个
    # print(eval(funcName))   这个会打印出函数返回值

# 测试刚刚的调用函数
callPackageFunc(funcsname)