# 结课大作业：改写平时作业3，采用生成器方式生成相应随机数
import math
import random

def MCC(func):
    def MCC_wrapper(*args,**kwargs):
        iter_result=func(*args,**kwargs)
        for i in range(0,args[0]-1):        #args[0]是num
            next(iter_result)               #8,9,10行：遍历生成器，运用next()方法，把最终的生成的随机数结果赋值给data
        data=next(iter_result)
        print("data_len:",len(data))
        print("final_random_data:",data)
        TP = FP = FN = TN = 0
        num = len(data)                #len(data)==args[0]==num
        for i in range(0, num):
            if data[i][0] == 0:
                if data[i][1] == 1:
                    FN += 1
                else:
                    TN += 1
            else:
                if data[i][1] == 1:
                    TP += 1
                else:
                    FP += 1
        multi_add_sum = (TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)
        if multi_add_sum==0:   #如果任意TP,FP,FN,FN四项，任意两项为零，那么设multi_add_sum为1
            multi_add_sum=1
        MCC = (TP * TN - FP * FN) / math.sqrt(multi_add_sum)
        print("MCC_result:")
        return MCC
    return MCC_wrapper

def ACC(func):
    def ACC_wrapper(*args,**kwargs):
        iterresult = func(*args, **kwargs)
        # print("num:",args[0])
        for i in range(0, args[0] - 1):       #args[0]是num
            next(iterresult)
        data = next(iterresult)
        print("data_len:", len(data))
        print("final_random_data:", data)
        correct_num = 0
        total_num = len(data)                #len(data)==args[0]==num
        for i in range(0, total_num):
            if data[i][0] == data[i][1]:
                  correct_num += 1
        accuracy=correct_num/total_num
        print("ACC_result:")
        return accuracy
    return ACC_wrapper

@MCC
def structDataSampling(num,**Kwargs):
    result=list()
    for item in range(0,num):
        for key,value in Kwargs["struct"].items():
            if key=="int":
                tmp=[]                            #用tmp接受随机生成一组二分类的bool值，即tmp=[bool,bool]
                for numitem in range(0,2):
                  it = iter(value['datarange'])
                  re=random.randint(next(it), next(it))
                  tmp.append(re)
            elif key=="float":
                it=iter(value['datarange'])
                tmp=random.uniform(next(it),next(it))
            elif key=="str":
                tmp=''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
        result.append(tmp)
        yield result

result=structDataSampling(1000,**{"struct":{"int":{"datarange":(0,1)}}})
print(result)