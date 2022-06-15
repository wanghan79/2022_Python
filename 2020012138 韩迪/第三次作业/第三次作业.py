# coding = utf-8
"""
    *NOTICE: THIS PROGRAM IS MADE BY WILLIAM FRIEDEBURG IN NENU
    *THIS PROGRAM INCLUDES A GUI
"""

import tkinter as tk
from tkinter.ttk import *
import random
from functools import wraps
from math import sqrt

global MCC
global ACC

def wrapACC(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        global ACC
        cnt = 0
        data = f(*args, **kwargs)
        for i in range(len(data)):
            if data[i][0] == data[i][1]:
                cnt += 1
        ACC = cnt / Num
        return data

    return wrap


def wrapMCC(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        global MCC
        data = f(*args, **kwargs)
        tp = fp = tn = fn = 0
        for item in data:
            if item[0] & item[1]:
                tp += 1
            elif item[0] & (~item[1]):
                fp += 1
            elif ~item[0] & ~item[1]:
                tn += 1
            elif ~item[0] & item[1]:
                fn += 1
        numerator = (tp * tn) - (fp * fn)
        denominator = sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        MCC = numerator / denominator
        return data

    return wrap


@wrapACC
def ACC_Simulation(num) -> list:
    retV = list()
    for i in range(num):
        retV.append([random.choice([True, False]), random.choice([True, False])])
    return retV


@wrapMCC
def MCC_Simulation(num) -> list:
    retV = list()
    for i in range(num):
        retV.append([random.choice([True, False]), random.choice([True, False])])
    return retV

def createGUI(Num,MCC,ACC):
    try:
        root = tk.Tk()
        Label(text="Python第三次作业").grid(column=0,row=0)
        Label(text="当前随机输入值{}".format(Num)).grid(column=1, row=0)
        Label(text="ACC:").grid(column=0, row=1)
        Label(text="{}".format(ACC)).grid(column=1, row=1)
        Label(text="MCC:").grid(column=0, row=2)
        Label(text="{}".format(MCC)).grid(column=1, row=2)
        root.mainloop()
    except :
        print('创建窗口失败，进入命令行模式！')
        print("当前随机输入值：{}".format(Num))
        print("ACC = {}".format(ACC))
        print("MCC = {}".format(MCC))

Num = int(random.random()*10000)

ACC_Simulation(Num)
MCC_Simulation(Num)

createGUI(Num,ACC,MCC)
