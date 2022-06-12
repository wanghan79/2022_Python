"""
    Author: STCloudLake
"""
import funlib.Functions as Functions

func = Functions.txtFileReader("funclist.txt")

def callOutsideFunc(funcName: str):
    for f in funcName:
        print(eval(f))

callOutsideFunc(func)