import random


def getSamples(**keys):
    samples = []
    for i in range(0, keys['num']):
        sample = []
        for key, value in keys['struct'].items():
            if key == "int":
                daterange = iter(value['datarange'])
                sample.append(random.randint(next(daterange), next(daterange)))
            elif key == "float":
                daterange = iter(value['datarange'])
                sample.append(random.uniform(next(daterange), next(daterange)))
            elif key == "str":
                sample.append(''.join(random.choice(value['datarange']) for i in range(value['len'])))
            else:
                break
        samples.append(sample)
    return samples


if __name__ == '__main__':
    with open("./struct.txt", encoding='utf-8') as f:
        struct = eval(f.read())
    result = getSamples(**struct)
    for item in result:
        print(item)
