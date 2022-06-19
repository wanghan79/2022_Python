def funcA():
    print("funcA")
def funcB():
    print("funcB")
def funcC():
    print("funcC")
def funcD():
    print("funcD")

#以下将函数封装入字典便于使用
# funcs={"a":funcA,"b":funcB,"c":funcC,"d":funcD}
# def callfuncs(action):
#     funcs[action]()
# callfuncs("a")