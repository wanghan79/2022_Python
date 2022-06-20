# 作业2
import funcs
def txtFileReader(file):
     listfiles=[]
     with open(file) as f:
         for line in f:
             listfiles.append(line)
     f.close()
     return listfiles


#  step1: read a config txt file, obtaining function name
funcsname=txtFileReader("functionlist.txt")

#  step2: define a function to call the functions in the package
def callPakageFunc(funcName: str):
  print(eval(funcName))


#  step3: test the function define in step2
callPakageFunc(funcsname.pop())

"""
# 1、读取文本文件中函数名，如果是funB没有返回值，所以eval没有返回值会输出”None“，如果funB有返回值，则输出返回值内容

# 2、可以在functionlist.txt增加多行
    funcs.funcA()
    funcs.funcB()
    funcs.funcC()
    ......
    # 则step2、step3改写为：
def callPakageFunc(funcName:str):
    for  func in funcName:
         print(eval(func))

callPakageFunc(funcsname)

"""