# 函数封装:具体执行过程
# 类封装:面向对象
# 包:面向用户应用

import funcLib.funcs as funcs

# func=funcs.funcA()

func = funcs.txtFileReader("config.txt")


def callOutsideFunc(funcName: str):
    print(eval(funcName))


callOutsideFunc(func.pop())
