import functions


def getfunctions(path):
    with open(path, "r") as f:
        text = f.read()
    return text.split()


functionNames = getfunctions("second.txt")

for functionName in functionNames:
    eval("functions." + functionName)()