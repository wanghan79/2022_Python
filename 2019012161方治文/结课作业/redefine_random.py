import random


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
                    element.append("unkonwn")
            yield element