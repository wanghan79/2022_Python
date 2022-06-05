import json
import random
import string
from itertools import cycle
from pprint import pprint


def gen_int(range: tuple = (0, 100)):
    '''
    :param length: min and max, defaults to 0, 100
    :return: random int
    '''
    range = (0, 100) if range is None else range
    return random.randint(*range)


def gen_float(range: tuple = (0, 1)):
    '''
    :param length: min and max, defaults to 0, 1
    :return: random float
    '''
    range = (0, 1) if range is None else range
    return random.uniform(*range)


def gen_str(length: tuple = (8, 8),
            data: str = string.ascii_letters + string.digits):
    '''
    :param length: min and max string length, defaults to 8
    :param data: string charset, defaults to ascii_letters + digits
    :return: random string
    '''
    length = (8, 8) if length is None else length
    data = (string.ascii_letters + string.digits) if data is None else data
    return ''.join(random.choices(data, k=random.randint(*length)))


def gen_list(struct: dict, length: int):
    '''
    :param struct: list struct data
    :param length: list length: (min_length, max_length)
    :return: list with random data
    '''
    index = cycle(range(len(struct)))
    length = random.randint(*length)
    loop_index = [next(index) for _ in range(length)]

    result = []
    for i in loop_index:
        result.append(gen_struct(struct[i]))
    return result


def gen_struct(struct: dict):
    '''
    :param struct: struct data
    :return: struct with data
    '''
    _type = struct['type']
    _range = struct.get('range')

    if isinstance(_range, int):
        _range = (_range, _range)

    if _type == 'list':
        return gen_list(struct['struct'], _range)
    elif _type == 'tuple':
        return tuple(gen_list(struct['struct'], _range))
    elif _type == 'int':
        return gen_int(_range)
    elif _type == 'float':
        return gen_float(_range)
    elif _type == 'str':
        return gen_str(_range, struct.get('data'))


def struct_sampling(num: int, **kwargs):
    '''
    :param num: numbers of struct to generate
    :return: list of structs
    '''
    res = []
    for _ in range(num):
        res.append(gen_struct(kwargs))
    return res


if __name__ == '__main__':
    with open('./struct.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i, struct in enumerate(struct_sampling(5, **data)):
        print(f'Sample {i}')
        pprint(struct)
        print()
