"""
Random structured data generator
@author STCloudLake
"""
import random


def structuredDataSampling(**kwargs):
    """
    The function is to generate corresponding random data according to the given requirements
    :param kwargs: A template for describing the generated data structure
        A standard template shall be in the following format:
        {"num":10,"struct":{"int":{"datarange":(0,100)},"float":{"datarange":(0,100)},"str":{"datarange":string.ascii_uppercase,"len":100}}}
        'num' specifies the number of structures generated
        'struct' specifies the style of structures generated, includes:
            (Optional)'int':{"datarange":(a,b)}
                which a is the minimum and b is the maximum
            (Optional)'float':{"datarange":(a,b)}
                which a is the minimum and b is the maximum
            (Optional)'str':{"datarange":characterSet,"len":strlen}
                which character specifies the characters will be contained in the generated string,
                strlen specifies the length of the generated string
    :return: A set of data samples generated according to the template data structure
    """
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
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def apply():
    externalTxtTemplateFile = open("data/dataTemplate.txt")
    para = eval(externalTxtTemplateFile.read())
    result = structuredDataSampling(**para)
    for item in result:
        print(item)


apply()
