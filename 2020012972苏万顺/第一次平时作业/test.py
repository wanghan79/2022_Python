"""
Author: WanshunSu 2020012972
Purpose: First python class homework in spring semester, 2022
Introduction:
           It and 'Random_Generator_Funciton.py' and 'Random_Generator_Function_Iterator.py' and
           'Random_Generator_Class_Decorator.py' file as a whole.
           You can run the .py file directly to test 'Random_Generator_Funciton.py' and
           'Random_Generator_Function_Iterator.py' and 'Random_Generator_Class_Decorator.py' .
           If you want to know more about the internal implementation of random numbers or strings generation,
           please go to check 'Random_Generator_Funciton.py' and 'Random_Generator_Function_Iterator.py' and
           'Random_Generator_Class_Decorator.py' file.
Created:2022/5/29
"""
from Random_Generator_Class_Decorator import Random_Generator_Class_Decorator
from Random_Generator_Function_Decorator import Random_Generator_Function_Decorator
from Random_Generator_Funciton import structDataSampling
import string
def txtFileToDataStrcut(filename):
    with open(filename, "r") as f:
        line = f.readlines()
    kw = {}
    data = {}
    for i in line:
        word = i.split()
        if len(word) == 1:
            num = int(word[0])
            kw["num"] = num
            continue
        type = word[0]
        if type == "int":
            data[type] = {"datarange": (int(word[1]), int(word[2]))}
        elif type == "float":
            data[type] = {"datarange": (float(word[1]), float(word[2]))}
        elif type == "str":
            data[type] = {"datarange": word[1], "strlen": int(word[2])}
        else:
            print("Occur Error")
            continue
        kw['struct']=data
        f.close()
    return kw

print('######################################test1##############################################')
kwargs = txtFileToDataStrcut("data.txt")
result = structDataSampling(**kwargs)
print('############################')
print("The dict in the file is: ", kwargs)
print("The generated data is:")
for item in result:
    print(item)
print('############################')

print('######################################test2##############################################')
kwargs = txtFileToDataStrcut("data.txt")
print('############################')
print("The dict in the file is: ", kwargs)
@Random_Generator_Function_Decorator("Random_Function_Decorator")
def test2(**dic):
    pass
test2(**kwargs)
print('############################')

print('######################################test3##############################################')
kwargs = txtFileToDataStrcut("data.txt")
@Random_Generator_Class_Decorator(**kwargs)
def test3(res):
    for item in res:
        print(item)
print('############################')
print("The dict in the file is: ", kwargs)
test3()
print('############################')