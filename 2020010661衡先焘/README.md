### 运行结果

平时作业

```python
C:\Users\11468\Desktop\2020010661衡先焘\第1次平时作业>python Main.py
===第1次平时作业===
读取文件完成
随机结构: {'int': {'range': (10, 20)}, 'float': {'range': (100.0, 200.0)}, 'str': {'range': 'abcdefgABCDEFG1234567890!@#$%^&*()_.+', 'length': 10}}
[20, 168.2156241349325, 'acGc6f_$E&']
[17, 177.81248343169773, '+&fGgbb.BG']
[14, 129.30419094307805, '**!B(GE(a$']
[14, 179.23663546878777, 'CA9GGDE@c.']
[13, 181.72010165178338, '4371_9D0a#']


C:\Users\11468\Desktop\2020010661衡先焘\第2次平时作业>python Main.py
===第2次平时作业===
读取文件完成
这是我的函数A
这是我的函数B
这是我的函数B

C:\Users\11468\Desktop\2020010661衡先焘\第3次平时作业>python Main.py
===第三次平时作业===
Accuracy: 49.50%
Accuracy: 48.20%
Accuracy: 48.20%
MCC: -3.57%

```

<br/>

期末大作业

```python
C:\Users\11468\Desktop\2020010661衡先焘\结课作业>python Main.py
util.RandomDataUtil - INFO: 读取文件完成
util.RandomDataUtil - INFO: 随机结构: {'tuple': {'range': [(0, 0), (0, 1), (1, 0), (1, 1)], 'length': 10000}}

decorator.BaseCC - INFO: the function acc () is running...
decorator.BaseCC - INFO: 修饰器ACC执行
decorator.ACC - INFO: 第1波数据 --> ACC: 50.67%
decorator.ACC - INFO: 第2波数据 --> ACC: 49.99%
decorator.ACC - INFO: 第3波数据 --> ACC: 50.18%
decorator.ACC - INFO: 第4波数据 --> ACC: 49.56%
decorator.ACC - INFO: 第5波数据 --> ACC: 50.49%
decorator.ACC - INFO: 第6波数据 --> ACC: 50.19%
decorator.ACC - INFO: 第7波数据 --> ACC: 49.48%
decorator.ACC - INFO: 第8波数据 --> ACC: 50.56%
decorator.ACC - INFO: 第9波数据 --> ACC: 50.07%
decorator.ACC - INFO: 第10波数据 --> ACC: 49.97%
decorator.ACC - INFO: 所有数据一共有的 --> ACC: 50.12%

decorator.BaseCC - INFO: the function mcc () is running...
decorator.BaseCC - INFO: 修饰器MCC执行
decorator.MCC - INFO: 第1波数据 --> MCC: 1.66%
decorator.MCC - INFO: 第2波数据 --> MCC: 1.40%
decorator.MCC - INFO: 所有数据一共有的 --> MCC: 1.53%

decorator.BaseCC - INFO: the function cc () is running...
decorator.BaseCC - INFO: 修饰器CC执行
decorator.CC - INFO: 第1波数据 --> ACC: 50.31%
decorator.CC - INFO: 第1波数据 --> MCC: 0.62%
decorator.CC - INFO: 第2波数据 --> ACC: 50.54%
decorator.CC - INFO: 第2波数据 --> MCC: 1.09%
decorator.CC - INFO: 所有数据一共有的 --> ACC: 50.42%
decorator.CC - INFO: 所有数据一共有的 --> MCC: 0.85%

Current memory usage is 0.291MB; Peak was 0.379MB
```

<br/>

### 内存对比

前提条件: 元组数组有10000个(0, 0), 即意味着每波数据有10000个

10波数据时

|        | 当前内存使用  | 内存使用峰值  |
|--------|---------|---------|
| yield  | 0.11MB  | 0.198MB |
| return | 0.109MB | 0.897MB |


20波数据

|        | 当前内存使用  | 内存使用峰值   |
|--------|---------|----------|
| yield  | 0.112MB | 0.2MB    |
| return | 0.11MB  | 1.774.MB |

不难看出yield方式提高了使用的上限，内存峰值几乎保持不变。
而直接append上所有的数据，会导致内存峰值急剧上升。
