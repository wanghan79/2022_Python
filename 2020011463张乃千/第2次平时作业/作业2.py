import myFuncs.testfunc as funcs

def readFunctionsName(path:str):
    with open(path, "r") as f:
        textOfFunctions = f.read()
    return textOfFunctions.split()

functionNames = readFunctionsName("functlist.txt")

for functionName in functionNames:
    eval("funcs."+functionName)()
