"""
Author:WanshunSu
Purpose: Second python class homework in spring semester, 2022
Introduction:
Created:2022/4/30
"""
def funcA():
    print("This is funcA")

def funcB():
    print("This is funcB")

def funcC():
    print("This is funcC")

def funcD():
    print("This is funcD")

def txtFileReader(file):
    lstfiles = []
    with open(file) as f:
        for line in f:
            lstfiles.append(line)
    f.close()
    return lstfiles

funcs={"a":funcA,"b":funcB,"c":funcC,"d":funcD,"e":txtFileReader}

# def callfuncs(action):
#     funcs[action]()
#
# callfuncs("e")
