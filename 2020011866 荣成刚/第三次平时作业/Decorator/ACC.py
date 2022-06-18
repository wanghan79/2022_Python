
# ACC= （TP+TN）/（ TP+TN+FP+FN）

class DecoratorAcc:
    def __init__(self, func):
        self._func = func
        self.struct = None

    def __call__(self, *args, **kwargs):
        self.struct = self._func(*args, **kwargs)
        calculate_value = self.__calculate__()
        print("Accuracy的值为: {:.2%}".format(calculate_value))

    def __calculate__(self):
        tp_tn = self.struct[0] + self.struct[1]
        length = self.struct[0] + self.struct[1] + self.struct[2] + self.struct[3]
        return tp_tn / length
