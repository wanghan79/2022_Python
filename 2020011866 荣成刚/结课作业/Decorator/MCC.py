import math


# Matthews−score(MCC) =（TP∗TN−FP∗FN）/sqrt((TP + FP)(FN + TP)(FN + TN)(FP + TN))

class DecoratorMcc:
    def __init__(self, func):
        self._func = func
        self.struct = None

    def __call__(self, *args, **kwargs):
        self.struct = self._func(*args, **kwargs)
        calculate_value = self.__calculate__()
        print("MCC计算值为: {:.2%}".format(calculate_value))

    def __calculate__(self):
        tp_tn_fp_fn = self.struct[0] * self.struct[1] - self.struct[2] * self.struct[3]
        tfft_ftft = (self.struct[0] + self.struct[2]) * (self.struct[3] * self.struct[0]) * \
                    (self.struct[3] + self.struct[1]) * (self.struct[2] + self.struct[1])
        return tp_tn_fp_fn / math.sqrt(tfft_ftft)
