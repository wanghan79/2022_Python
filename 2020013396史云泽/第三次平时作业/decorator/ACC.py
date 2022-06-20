class Decorator:
    def __init__(self, func):
        self._func = func
        self.struct = None

    def __call__(self, *args, **kwargs):
        self.struct = self._func(*args, **kwargs)
        core_value = self.__core__()
        print("Accuracy: {:.2%}".format(core_value))
        return self.struct

    def __core__(self):
        data_list = list()
        tp_tn = 0
        for i in self.struct:
            data_list.append(not i[0] ^ i[1])
            if not i[0] ^ i[1]:
                tp_tn += 1
        return tp_tn / len(self.struct)
