# coding = utf-8
"""
    *NOTICE: THIS PROGRAM IS MADE BY WILLIAM FRIEDEBURG IN NENU
    *THIS PROGRAM INCLUDES A GUI WITH MULTI THREADS
"""
import random
from functools import wraps
import math
import tkinter as tk
from time import sleep
from tkinter.ttk import *
import threading

global ACC
global MCC
global argument
argument = {"num": 100, "struct": {"bool": {"num": 20}}}
global root


class Random:
    def __init__(self, **kwargs):
        self.num = kwargs["num"]
        self.struct = kwargs["struct"]

    def __iter__(self):
        for i in range(self.num):
            if i == self.num:
                raise StopIteration
            element = list()
            for key, val in self.struct.items():
                if key == "int":
                    it = iter(val["range"])
                    element.append(random.randint(next(it), next(it)))
                elif key == "float":
                    it = iter(val["range"])
                    element.append(random.uniform(next(it), next(it)))
                elif key == "str":
                    strRange = val["range"]
                    strLength = val["length"]
                    string = ""
                    for j in range(strLength):
                        string += random.choice(strRange)
                    element.append(string)
                elif key == "bool":
                    for ith in range(val["num"]):
                        element.append(random.choice((True, False)))
                else:
                    element.append("未知")
            yield element


def decorateWith(calcType):
    def decorator(func):
        wraps(func)

        def wrapper(*args, **kwargs):
            global ACC
            global MCC
            result = func(*args, **kwargs)
            total = len(result)
            TP = TN = FP = FN = 0
            for element in result:
                if (element[0] is True) and (element[1] is True):
                    TP += 1
                elif (element[0] is True) and (element[1] is False):
                    FN += 1
                elif (element[0] is False) and (element[1] is True):
                    FP += 1
                elif (element[0] is False) and (element[1] is False):
                    TN += 1
                else:
                    pass
            if calcType == "ACC":
                ACC = (TP + TN) / total
            elif calcType == "MCC":
                denominator = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
                if (denominator == 0):
                    denominator = 1
                MCC = (TP * TN - FP * FN) / denominator
            else:
                pass
            return result

        return wrapper

    return decorator


@decorateWith("MCC")
@decorateWith("ACC")
def getRandoms(**kwargs):
    generator = Random(**kwargs)
    resultList = []
    for element in generator:
        resultList.append(element)
    return resultList


threads = list()
threadCalc = threading.Thread(target=getRandoms, kwargs=argument)
threads.append(threadCalc)

for th in threads:
    th.setDaemon(True)
    th.start()

for th in threads:
    th.join()

try:
    root = tk.Tk()
    Label(text="Python结课大作业").grid(column=0, row=0)
    Label(text=str(argument)).grid(column=1, row=0)
    Label(text="ACC:").grid(column=0, row=1)
    Label(text="{}".format(ACC)).grid(column=1, row=1)
    Label(text="MCC:").grid(column=0, row=2)
    Label(text="{}".format(MCC)).grid(column=1, row=2)
    root.mainloop()
except:
    print("ERROR!当前系统不支持GUI模式，自动切换为命令行模式！")
    print("当前输入的随机参数为：{}".format(str(argument)))
    print("ACC={}".format(ACC))
    print("MCC={}".format(MCC))
