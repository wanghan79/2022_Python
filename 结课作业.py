# coding = utf-8
import random
import tkinter as tk
from math import sqrt
from tkinter.ttk import *

global MCC
global ACC


def wrapaCC(f):
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


def wrapmCC(f):
    def wrap(*args, **kwargs):
        global MCC
        data = f(*args, **kwargs)
        tp = 0
        fp = 0
        tn = 0
        fn = 0
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


def intNum():
    for i in range(10000):
        yield i


def get_random_rang():
    for i in range(1, 10000):
        if random.randint(1, 10) > 9:
            yield i
        else:
            continue


@wrapaCC
def ACC_Simulation(num):
    retx = []
    for i in range(num):
        retx.append([random.choice([True, False]), random.choice([True, False])])
    return retx


@wrapmCC
def MCC_Simulation(num):
    retV = []
    for i in range(num):
        retV.append([random.choice([True, False]), random.choice([True, False])])
    return retV


def createGUI(Num, MCC, ACC):
    root = tk.Tk()
    # 获取屏幕宽高
    width = int(root.winfo_screenwidth() / 2)
    height = int(root.winfo_screenheight() / 2)
    root.geometry(f'{width}x{height}')

    # 计算中心坐标点
    screen_width = root.winfo_screenwidth() / 2 - width / 2
    screen_height = root.winfo_screenheight() / 2 - height / 2

    # 移动窗口
    root.geometry(f"+{int(screen_width)}+{int(screen_height)}")
    Label(text = "Python第四次作业").pack()
    Label(text = "当前随机输入值{}".format(Num)).pack()
    Label(text = "ACC:").pack()
    Label(text = "{}".format(ACC)).pack()
    Label(text = "MCC:").pack()
    Label(text = "{}".format(MCC)).pack()
    root.mainloop()


Num = get_random_rang().__next__()
ACC_Simulation(Num)
MCC_Simulation(Num)

createGUI(Num, ACC, MCC)
