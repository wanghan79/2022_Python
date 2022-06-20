import funcCollection.funcs as funcs

func = funcs.txtFileReader("config.txt")



def callOutsideFunc(funcName: str):
    eval(funcName)


callOutsideFunc(func.pop())
