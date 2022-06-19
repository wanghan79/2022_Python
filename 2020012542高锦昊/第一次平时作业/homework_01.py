import random


def getSamples(**kwargs):
    samples = []
    for i in range(0, kwargs['num']):
        sample = []
        for key, value in kwargs['struct'].items():
            if key == "int":
                dataRange = iter(value['datarange'])
                sample.append(random.randint(next(dataRange), next(dataRange)))
            elif key == "float":
                dataRange = iter(value['datarange'])
                sample.append(random.uniform(next(dataRange), next(dataRange)))
            elif key == "str":
                sample.append(''.join(random.choice(value['datarange']) for i in range(value['len'])))
            else:
                break
        samples.append(sample)
    return samples


with open("data.txt", encoding='utf-8') as f:
    struct = eval(f.read())
resultsList = getSamples(**struct)
for result in resultsList:
    print(result)
