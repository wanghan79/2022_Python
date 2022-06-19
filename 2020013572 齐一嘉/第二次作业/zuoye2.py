import h2.test1 as funcs


def readFunctionsName(path: str):
    with open(path, "r") as f:
        textOfFunctions = f.read()
    return textOfFunctions.split()


functionNames = readFunctionsName("functlist")

for functionName in functionNames:
    eval("funcs." + functionName)()