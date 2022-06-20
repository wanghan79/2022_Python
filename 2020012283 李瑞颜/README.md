# 2022_Python



## 第一次作业

- 作业要求

编写一个函数，生成给定个数的数据结构的随机数据，要求使用关键字参数给定数据结构，并从外部文本文件中读取相应数据结构的字典作为关键字参数传入函数。

- 描述

  ```txt
  homework1.py 含有3个函数
  	* structDataSampling(**kwargs) 随机生成数据结构
  	* txtFileReader(file) 读取文件
          * apply() 运行structDataSampling方法并打印值
  liry.txt 为外部文本文件
  ```



## 第二次作业

- 作业要求

编写一个Python包，包里提供若干函数，再写一个py文件，通过读取文本文件中指定的函数名，能够调用该包中的函数。 

- 描述  

```txt
funcCollection  
 	- functions.py 包含4个函数的py文件
config.txt  函数的文本表示
do.py  含有2个函数  
	* txtFileReader(file) 读取文件
        * callBackFunc(funcList) 执行funcList内的内容
```



## 第三次作业

- 作业要求

采用修饰器的方式对模拟二分类预测结果的精度和马修相关系数进行计算，模拟预测结果采用随机数生成函数作为被修饰函数。 

- 描述

  ```txt
  homework3.py 含有三个函数
  	* Decorator(level) 函数修饰器，根据level选择ACC修饰或MCC修饰，含有3个子函数
             	# ACC(data) 计算ACC
             	# MCC(data) 计算MCC
             	# wrap1(func) 嵌套函数，在得到原函数的结果后，根据level为ACC或MCC计算并得出结果
  	* structDataSampling_ACC(**kwargs) 使用ACC修饰的随机数据结构生成器
  	* structDataSampling_MCC(**kwargs) 使用MCC修饰的随机数据结构生成器
  	      
  ```

  

## 结课作业

- 作业要求

在平时作业三基础上，采用生成器方式生成相应随机数。



- 描述

   通过一系列查阅，在进行第三次作业时，实现了较容易理解的嵌套函数修饰器，但是函数嵌套显得很冗余。在进行结课作业编写时，通过将return 改为 yield 后，出现了一些列bug，如object of type 'generator' has no len()，以及输出值恒0为或1。在进行询问与参考后，对循环部分进行修改，同时更改为更加紧凑的类修饰器。

  ```txt
  finalWork.py 含有一个类修饰器，一个随机数据结构生成器
  	* ResultAnalysis 类
  		# __init__(self, func) 构造函数
  		# __call__(self, **kwargs) 在函数内部调用func，将kwargs传入func
  		# dataGenerate(self,data) 由于yield返回的是可迭代对象，所以我们无法多次使用数据，故需要先迭代可迭代对象将数据保存起来
      	        # ACC(self, TP, TN, FP, FN) 计算ACC
                 # MCCMCC(self, TP, TN, FP, FN) 计算MCC
        * structDataSampling(**kwargs) 随机数据结构生成器
  ```

  
