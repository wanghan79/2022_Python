import funlib.funcs as funcs

func = funcs.txtFileReader("config")


def callOutsideFunc(funcName: str):
    eval(funcName)


callOutsideFunc(func.pop())
