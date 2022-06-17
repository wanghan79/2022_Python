import my_package.trf as funcs

def readFunctionsName(path:str):
    with open(path,"r") as f:
        textOfFunctions=f.read()
    return textOfFunctions.split()

functionNames = readFunctionsName("name.txt")

for functionName in functionNames:
    eval("funcs."+functionName)()
