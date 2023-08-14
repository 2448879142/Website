# pyTorch入门

## 设置镜像源

~~~python
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
~~~

![1692022793846.png](https://img1.imgtp.com/2023/08/14/iH8Zav9V.png)

## 安装torch

终端安装深度学习包

~~~python
pip install torch
pip install numpy
~~~

![1692022925589.png](https://img1.imgtp.com/2023/08/14/g5igJWhZ.png)

![1692022972716.png](https://img1.imgtp.com/2023/08/14/2EmyX3Qd.png)

## 引入

创建py文件，引入torch包

~~~python
import torch
~~~

![1692022996309.png](https://img1.imgtp.com/2023/08/14/yIxOQoHv.png)

## 基本概念

### 张量、标量、向量、矩阵[^1]

- 张量这一概念的核心在于，它是一个数据容器。它包含的数据几乎总是数值数据，因此它是数字的容器。

- 矩阵，它是二维张量。张量是矩阵向任意维度的推广［注意，张量的维度（dimension）通常叫作轴（axis）］。

- 仅包含一个数字的张量叫作标量（scalar，也叫标量张量、零维张量、0D 张量）。在 Numpy中，一个 float32 或 float64 的数字就是一个标量张量（或标量数组）。你可以用 ndim 属性来查看一个 Numpy 张量的轴的个数。标量张量有 0 个轴（ ndim == 0 ）。张量轴的个数也叫作阶（rank）。下面是一个 Numpy 标量。

- 数字组成的数组叫作向量（vector）或一维张量（1D 张量）。一维张量只有一个轴。下面是一个 Numpy 向量。

- 向量组成的数组叫作矩阵（matrix）或二维张量（2D 张量）。矩阵有 2 个轴（通常叫作行和列）。你可以将矩阵直观地理解为数字组成的矩形网格。下面是一个 Numpy 矩阵。

~~~python
import torch
import numpy as np

x = torch.arange(12)
print(x)
print(x.ndim)

y = np.array(12)
print(y)
print(y.ndim)

z = np.arange(12)
print(z)
print(z.ndim)

l = np.array([[5, 78, 2, 34, 0],
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]])
print(l)
print(l.ndim)
~~~

~~~python
tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
1
12
0
[ 0  1  2  3  4  5  6  7  8  9 10 11]
1
[[ 5 78  2 34  0]
 [ 6 79  3 35  1]
 [ 7 80  4 36  2]]
2
~~~
[^1]: [什么是张量Tensor](https://blog.csdn.net/weixin_42259833/article/details/124766853)
### 函数

- `torch.randn`从正态分布（均值0，标准差1的标准高斯分布）中随机采样。

```python
x = torch.randn(3,4)
print(x)
print(x.ndim)

```
~~~
tensor([[-0.0054, -0.1882, -1.3362,  1.7293],
        [ 0.7074, -0.0288, -1.1412,  1.2299],
        [-0.7506, -0.2100, -2.2069,  0.4566]])
2
~~~

- `torch.tensor`为张量中每个元素赋予确定值。

```
x = torch.tensor([[2, 3, 1, 3, 1], [2, 3, 7, 5, 1]])
print(x)
print(x.ndim)
```

~~~
tensor([[2, 3, 1, 3, 1],
        [2, 3, 7, 5, 1]])
2
~~~

### 运算

1. 算术运算符：

- `+`：加法运算符
- `-`：减法运算符 
- `*`：乘法运算符
-  `/`：除法运算符（结果为小数）
- `%`：取余数运算符
-  `**`：乘方运算符

2. 比较运算符：

- `==`：检查两个值是否相等
-  `!=`：检查两个值是否不相等

- `>` ：检查一个值是否大于另一个值 

- `<`：检查一个值是否小于另一个值 

- `>=`：检查一个值是否大于或等于另一个值 

- `<=`：检查一个值是否小于或等于另一个值

3. 逻辑运算符： 

- and：逻辑与，当两个条件都为True时，返回True 

- or：逻辑或，当两个条件至少一个为True时，返回True 

- not：逻辑非，将True转换为False，将False转换为True

```python
x = torch.tensor([2, 3, 1, 3, 1])
y = torch.tensor([2, 3, 7, 5, 1])
print(x,y)
print(x.ndim,y.ndim)
print('--------求和--------')
print(x+y)
print((x+y).ndim)
print('--------求差--------')
print(x-y)
print((x-y).ndim)
print('--------求乘--------')
print(x*y)
print((x*y).ndim)
print('--------求除--------')
print(x/y)
print((x/y).ndim)
```

```
tensor([2, 3, 1, 3, 1]) tensor([2, 3, 7, 5, 1])
1 1
--------求和--------
tensor([4, 6, 8, 8, 2])
1
--------求差--------
tensor([ 0,  0, -6, -2,  0])
1
--------求乘--------
tensor([ 4,  9,  7, 15,  1])
1
--------求除--------
tensor([1.0000, 1.0000, 0.1429, 0.6000, 1.0000])
1
```

4. 指数`torch.exp()`

```python
x = torch.tensor([0,-1])
print(x)
print(1/math.e)
x = torch.exp(x)
print(x)
```

~~~
tensor([ 0, -1])
0.36787944117144233
tensor([1.0000, 0.3679])
~~~

## 节省内存

运行一些运算时，可能会分配新内存，例如Y=X+Y，会取消掉Y指向的张量，而是指向新分配的内存处的张量。

```python
before = id(Y)
Y=Y+X
id(Y)==before #False
```

这可能在某些时刻是我们不想看到的：

- 我们不总是想分配新的内存，在机器学习中，我们可能有数百兆参数，并且在一秒内多次更新所有参数，我们希望原地执行这些更新。
- 如果我们不原地更新参数，可能其他引用仍然会指向旧的内存位置，导致引用旧参。

解决办法：切片表示法，Y[:]=<expression>.Y[:]=X+Y

## 处理缺失值

“NaN”代表缺失值。典型办法：插值法、删除法。

插值法：利用同一列的均值替换“NaN”值。

删除法：直接忽略缺失值。

## 矩阵转置

交换矩阵的行和列

```python
A.T
```

### 对称矩阵

矩阵本身与其转置相等

```python
A==A.T
```

### 哈达玛积

两个矩阵的按元素乘法成为Hadamard积（Hadamard product）

```
A*B
```

## 点积（Dot Product）

两个向量的点积是相同位置的按元素乘积的和

给定一组向量X表示的值，和一组向量W表示的权重，X的值根据权重W的加权和，可以表示为点积X[^T]W.

[^T]:T表示点积。

[(126条消息) 矩阵篇（三）-- 矩阵的普通乘积、Hadamard 积、Kronecker 积及其性质_hadamard乘积_长路漫漫2021的博客-CSDN博客](https://blog.csdn.net/xq151750111/article/details/121049396)

## 范数

范数听起来很像距离的度量。

- L1范数是向量元素的绝对值之和。

- L2范数是向量元素平方和的平方根。





