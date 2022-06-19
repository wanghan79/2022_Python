from funcs import myfuncs

# 虽然调用包这个语句是灰色的，但是不可缺少（执行时还是用到了）

'''
作业要求：
    编写一个Python包，包里提供若干函数，再写一个py文件，通过读取文本文件中指定的函数名，能够调用该包中的函数。
'''


# 读取文件内容生成函数名列表
def txtFileReader(filePath):
    filesList = []
    with open(filePath) as f:
        for line in f:
            filesList.append(line)
    return filesList


# 根据函数名打印调用函数后的结果
def callPackageFuc(funcsNameList: list):
    for funcName in funcsNameList:
        # 先执行调用的函数，之后打印函数返回结果
        print(eval(funcName))
    print('=================================')
    for funcName in funcsNameList:
        # 只执行调用的函数，不接收返回值
        eval(funcName)


# 本文件运行时执行的代码
if __name__ == "__main__":
    myFuncsNameList = txtFileReader("./FunctionList.txt")
    callPackageFuc(myFuncsNameList)

'''
打印结果样例：
This is funcA
A
This is funcB
B
This is funcC
C
This is funcD
D
=================================
This is funcA
This is funcB
This is funcC
This is funcD

Process finished with exit code 0
'''