import funlib.funcs as funcs

func = funcs.txtFileReader("config.txt")

def callOutsideFunc(funcName:str):
    print(eval(funcName))

callOutsideFunc(func.pop())
