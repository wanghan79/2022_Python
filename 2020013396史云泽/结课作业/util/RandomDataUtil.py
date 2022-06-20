import random


def S_Generator(path="../data/data.txt"):
    with open(path, "r", encoding='utf-8') as f:
        structText = f.readlines()
    cin = {}
    for line in structText:
        if line.startswith("->"):
            break
        words = line.split()
        dataType = words[0]
        if dataType == "tuple":
            info = {}
            infoRange = []
            split = words[1].split("|")
            for string in split: infoRange.append(
                tuple([int(i) for i in string.replace('(', '').replace(')', '').split(',')]))
            info["range"] = infoRange
            info["length"] = int(words[2])
            cin["tuple"] = info
        else:
            continue
    return cin


class RSD_Generator:
    def __init__(self, num, **struct):
        self.num = num
        self.struct = struct

    def __iter__(self):
        if self.num <= 0:
            print("num should be a positive integer")
            return
        for i in range(self.num):
            element = list()
            tmp = None
            for key, val in self.struct.items():
                if key == "tuple":
                    strRange = val["range"]
                    strLength = val["length"]
                    tupleList = []
                    tmp = list()
                    for j in range(strLength):
                        tupleList.append(random.choice(strRange))
                    tmp.append(tupleList)
                    pass
                else:
                    element.append("Unknown Type!")
            yield tmp
