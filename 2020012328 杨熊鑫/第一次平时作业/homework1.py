import random
import string


# This function can generate random data according to the data structure of given parameters.
def generateRandomData(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            elif key == "bool":
                tmp = []
                for i in range(value['cnt']):
                    tmp.append(random.choice((True, False)))
                tmp = tuple(tmp)
            else:
                tmp = "unknown data type"
            element.append(tmp)
        result.append(element)
    return result


def generate():
    template = open("Template.txt")
    para = eval(template.read())
    result = generateRandomData(**para)
    for item in result:
        print(item)


if __name__ == "__main__":
    generate()
