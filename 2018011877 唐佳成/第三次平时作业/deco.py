from math import sqrt
from functools import reduce, wraps
from typing import Callable

def extract(data: list[tuple[bool, bool]]):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for x, y in data:
        if x == y:
            if x == True:
                tp = tp + 1
            else:
                tn = tn + 1
        else:
            if x == True:
                fn = fn + 1
            else:
                fp = fp + 1
    return (tp, tn, fp, fn)

def ACC(func: Callable[[int], list[tuple[bool, bool]]]):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        (tp, tn, fp, fn) = extract(data)
        return (tp + tn) / (tp + tn + fp + fn)
    return wrapper

def MCC(func: Callable[[int], list[tuple[bool, bool]]]):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        (tp, tn, fp, fn) = extract(data)
        return (tp * tn - tp * fn) / sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    return wrapper