"""
Author: WanshunSu 2020012972
Purpose: Third python class homework in spring semester, 2022
Introduction:
           It and 'Random_Generator_Function_Iterator.py' and 'Random_Generator_Class_Decorator.py'
           and 'ACC_MCC_Decorator.py' file as a whole.
           You can run the .py file directly to test 'Random_Generator_Function_Iterator.py' and
           'Random_Generator_Class_Decorator.py' and 'ACC_MCC_Decorator.py'.
           If you want to know more about the internal implementation of random numbers or strings generation,
           please go to check 'Random_Generator_Function_Iterator.py' and 'Random_Generator_Class_Decorator.py'
           and 'ACC_MCC_Decorator.py' file.
Created:2022/6/3
"""
from classandfunctionPack.Random_Generator_Class_Decorator import Random_Generator_Class_Decorator
from Random_Generator_Function_Decorator import structDataSampling
argument = {"num": 10000, "struct": {"bool": {"datarange": 2}}}

print('######################################test1##############################################')
print('############################')
structDataSampling(**argument)
print('############################')

print('######################################test2##############################################')
@Random_Generator_Class_Decorator(**argument)
def test2(res):
    pass
print('############################')
test2()
print('############################')