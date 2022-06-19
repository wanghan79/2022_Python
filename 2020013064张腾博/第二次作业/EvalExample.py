import funlib.funcs as funcs
# from funlib.funcs import funcA

# funcA()
func = funcs.txtFileReader("config.txt")


def callOutsideFunc(funcName: str):
    eval(funcName)


for item in func:
    callOutsideFunc(item)
