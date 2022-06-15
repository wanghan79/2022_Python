from Funcs import functions


def getfunctions(path):
    with open(path, "r") as f:
        text = f.read()
    return text.split()


functionNames = getfunctions("funclist.txt")

for functionName in functionNames:
    eval("functions." + functionName)()
