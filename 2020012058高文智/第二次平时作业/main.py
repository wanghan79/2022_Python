import functions

'''
平时作业二：编写一个Python包，包里提供若干函数，再写一个py文件，通过读取文本文件中指定的函数名，能够调用该包中的函数。
'''


def get_my_functions(path):
    with open(path, "r") as file:
        text = file.read()
    return text.split()


functionNames = get_my_functions("data.txt")

for fn in functionNames:
    eval("functions." + fn)()
