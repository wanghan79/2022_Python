import json

from deco import ACC, MCC
from struct_sampling import struct_sampling_yield

LENGTH = 10000

with open('./struct.json', 'r', encoding='utf-8') as f:
    struct = json.load(f)


@ACC
def pred1():
    return struct_sampling_yield(LENGTH, **struct)


print('Accuracy', pred1())


@MCC
def pred2():
    return struct_sampling_yield(LENGTH, **struct)


print('MCC', pred2())
