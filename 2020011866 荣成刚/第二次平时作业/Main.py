import funcsPackage.funcs as funcs

def txtFileReader(file):
    listfiles = []
    with open(file) as f:
        for line in f:
            listfiles.append(line)
    f.close()
    return listfiles

# 步骤一：读一个配置文本文件，给一个函数的名字


funcsname = txtFileReader("funclist.txt")


# 步骤二：定义一个函数，去调用包里面的函数


def callPackageFunc(funcName: str):
    print(eval(funcName))

# 步骤三：测试这个函数

callPackageFunc(funcsname.pop())
