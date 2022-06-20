from Function import function


def getfunctions(path):
    with open(path, "r") as f:
        text = f.read()
    return text.split()


funcNames = getfunctions("para.txt")
for functionName in funcNames:
    eval("function." + functionName)()
