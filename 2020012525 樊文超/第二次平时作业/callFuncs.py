from funcsPack import funcs

'''
    平时作业二：编写一个Python包，包里提供若干函数，再写一个py文件，
    通过读取文本文件中指定的函数名，能够调用该包中的函数。
'''

# 读取文件获取函数列表
def fileReadre(filePath):
    fileList = []
    with open(filePath) as f:
        for line in f:
            fileList.append(line)
    return fileList

# 根据函数名打印调用结果
def callFunc(funcNameList: list):
    for funcName in funcNameList:
        print('输出返回值：')
        print(eval(funcName))
    for funcName in funcNameList:
        eval(funcName)


if __name__ == "__main__":
    funcNameList = fileReadre('funcList.txt')
    callFunc(funcNameList)