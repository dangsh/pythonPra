import numpy as np

""" 多维数组

多维数组的类型是：numpy.ndarray。

使用numpy.array方法

以list或tuple变量为参数产生一维数组："""

# test1 = np.array([1,2,3,4])
# test1 = np.array((1.2,2,3,4))
# print(test1)
# print(type(test1))




"""以list或tuple变量为元素产生二维数组或者多维数组："""
# x = np.array(((1,2,3),(4,5,6)))  
# print(x)

# y = np.array([[1,2,3],[4,5,6]]) 
# print(y)




"""numpy数据类型设定与转换
numpy ndarray数据类型可以通过参数dtype 设定，
而且可以使用astype转换类型，在处理文件时候这个会很实用，
注意astype 调用会返回一个新的数组，也就是原始数据的一份拷贝"""

# numeric_strings2 = np.array(['1.23','2.34','3.45'],dtype=np.string_)
# # print(numeric_strings2)

# newTest = numeric_strings2.astype(float)
# print(newTest)





"""numpy索引与切片
index 和slicing ：第一数值类似数组横坐标，第二个为纵坐标"""
# x = np.array(((1,2,3),(4,5,6)))  
# print(x)
# print(x[1 , 2])
# print(x[:,0])
# print("------------------")
"""涉及改变相关问题 , 这是特别需要关注的！"""
# tempData = x[:,1]
# print(tempData)
# tempData[0] = 10
# print(tempData)
# print(x)
"""通过上面可以发现改变tempData会改变x ，
因而我们可以推断，tempData和x指向是同一块内存空间值，
系统没有为tempData 新开辟空间把x值赋值过去。"""


# arr = np.arange(10)
# print(arr)
# print(type(arr))
# print(arr[4])
# print(arr[3:6])
# arr[3:6] = 12
# print(arr)
"""如上所示：当将一个标量赋值给切片时，
该值会自动传播整个切片区域，
这个跟列表最重要本质区别，
数组切片是原始数组的视图，
视图上任何修改直接反映到源数据上面。
思考为什么这么设计？ 
Numpy 设计是为了处理大数据，
如果切片采用数据复制话会产生极大的性能和内存消耗问题。"""

"""假如说需要对数组是一份副本而不是视图可以如下操作"""
# arr_copy = arr[3:6].copy()
# print(arr_copy)
# arr_copy[:] = 24
# print(arr_copy)
# print(arr)




"""多维数组索引、切片"""
# arr2d = np.arange(1 , 10).reshape(3 , 3)
# print(arr2d)
# print(arr2d[2])
# print(arr2d[0][2])
# print(arr2d[0 , 2])



"""布尔型索引
这种类型在实际代码中出现比较多，关注下。"""
# names = np.array(["Bob" , "joe" , "Bob" , "will"])
# print(names)
# print(names == "Bob")




 
# a = [1, 2, 3, 4]     	#
# b = np.array(a)         	# array([1, 2, 3, 4])
# print(b)
# print(type(b))                   	# <type 'numpy.ndarray'>
 
# print(b.shape)                   	# (4,)
# print(b.argmax())                	# 3
# print(b.max())                   	# 4
# print(b.mean())                  	# 2.5
 
# c = [[2, 2], [13, 14]]  	# 二维列表
# d = np.array(c)         	# 二维numpy数组
# print(d)
# print(d.shape )                 	# (2, 2)
# print(d.size )                   	# 4
# print(d.max(axis=0))             	# 纵向最大值
# print(d.max(axis=1))            	# 横向最大值
# print(d.mean(axis=0))          	# 纵向平均值
# print(d.mean(axis=1))          	# 横向平均值
# print(d.flatten())              	# 展开一个numpy数组为1维数组，array([1, 2, 3, 4])
# print(np.ravel(c))                # 展开一个可以解析的结构为1维数组，array([1, 2, 3, 4])
 



# # 3x3的浮点型2维数组，并且初始化所有元素值为1
# e = np.ones((3, 3), dtype=np.float)
# print(e)
 
# 创建一个一维数组，元素值是把3重复4次，array([3, 3, 3, 3])
# f = np.repeat(3, 4)
# print(f)
 
# 2x2x3的无符号8位整型3维数组，并且初始化所有元素值为0
# g = np.zeros((2, 2, 3), dtype=np.uint8)
# print(g)
# print(g.shape )                  # (2, 2, 3)
# h = g.astype(np.float)  # 用另一种类型表示
# print(h)
 
# l = np.arange(10)      	# 类似range，array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(l)


# m = np.linspace(0, 6, 5)# 等差数列，0到6之间5个取值，array([ 0., 1.5, 3., 4.5, 6.])
# print(m)




# 将数据保存到文件
# p = np.array(
#     [[1, 2, 3, 4],
#      [5, 6, 7, 8]]
# )
# print(p)
 
# np.save('p.npy', p)     # 保存到文件
# q = np.load('p.npy')    # 从文件读取
# print(q)




"""作为一种多维数组结构，array的数组相关操作是非常丰富的："""
'''
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],
 
       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
'''
# a = np.arange(24).reshape((2, 3, 4))
# print(a)
# print("------------------------")
# b = a[1][1][1]  # 17
# print(b)
 
'''
array([[ 8,  9, 10, 11],
       [20, 21, 22, 23]])
'''
# c = a[:, 2, :]
# print(c)


''' 用:表示当前维度上所有下标
array([[ 1,  5,  9],
       [13, 17, 21]])
'''
# d = a[:, :, 1]
# print(d)
 
''' 用...表示没有明确指出的维度
array([[ 1,  5,  9],
       [13, 17, 21]])
'''
# e = a[..., 2]
# print(e)
 
'''
array([[[ 5,  6],
        [ 9, 10]],
 
       [[17, 18],
        [21, 22]]])
'''
# a:b 从a到b
# f = a[:, 1:, 1:-1]
# print(f)
 
'''
平均分成3份
[array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
'''
# gg = np.arange(9)
# print(gg)
# g = np.split(gg, 3)
# print(g)
 
'''
按照下标位置进行划分
[array([0, 1]), array([2, 3, 4, 5]), array([6, 7, 8])]
'''
# hh = np.arange(9)
# print(hh)
# h = np.split(hh, [2, -3])
# print(h)
 
# 快速构建范围内数组
# l0 = np.arange(6).reshape((2, 3))
# print(l0)
# l1 = np.arange(6, 12).reshape((2, 3))
# print(l1)
# print("-------------------------")
 
'''
vstack是指沿着纵轴拼接两个array，vertical
hstack是指沿着横轴拼接两个array，horizontal
更广义的拼接用concatenate实现，horizontal后的两句依次等效于vstack和hstack
stack不是拼接而是在输入array的基础上增加一个新的维度
'''
# m = np.vstack((l0, l1))
# print(m)
# p = np.hstack((l0, l1))
# print(p)
# q = np.concatenate((l0, l1)) # 纵向上拼接
# print(q)
# r = np.concatenate((l0, l1), axis=-1) # 横向上拼接
# print(r)
# s = np.stack((l0, l1))
# print(s)
# print("-------------------------")
 



'''
按指定轴进行转置
array([[[ 0,  3],
        [ 6,  9]],
 
       [[ 1,  4],
        [ 7, 10]],
 
       [[ 2,  5],
        [ 8, 11]]])
'''
# t = s.transpose((2, 0, 1))
# print(t)
 
'''
默认转置将维度倒序，对于2维就是横纵轴互换
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
'''
# u = a[0].transpose()	# 或者u=a[0].T也是获得转置
# print(u)
 
'''
逆时针旋转90度，第二个参数是旋转次数
array([[ 3,  2,  1,  0],
       [ 7,  6,  5,  4],
       [11, 10,  9,  8]])
'''
# v = np.rot90(u, 3)
# print(v)
 
'''
沿纵轴左右翻转
array([[ 8,  4,  0],
       [ 9,  5,  1],
       [10,  6,  2],
       [11,  7,  3]])
'''
# w = np.fliplr(u)
# print(w)
 
'''
沿水平轴上下翻转
array([[ 3,  7, 11],
       [ 2,  6, 10],
       [ 1,  5,  9],
       [ 0,  4,  8]])
'''
# x = np.flipud(u)
# print(x)
 
'''
按照一维顺序滚动位移
array([[11,  0,  4],
       [ 8,  1,  5],
       [ 9,  2,  6],
       [10,  3,  7]])
'''
# y = np.roll(u, 1)
# print(y)
 
'''
按照指定轴滚动位移
array([[ 8,  0,  4],
       [ 9,  1,  5],
       [10,  2,  6],
       [11,  3,  7]])
'''
# 0 行位移
# 1 列位移
# z = np.roll(u, 1, axis=0)
# print(z)
"""对于一维的array所有Python列表支持的下标相关的方法array也都支持，
所以在此没有特别列出"""






"""既然叫numerical python，
基础数学运算也是强大的"""
# 绝对值，1
# a = np.abs(-1)
# print(a)
 
# sin函数，1.0
# b = np.sin(np.pi/2)
# print(b)
 
# tanh逆函数，0.50000107157840523
# c = np.arctanh(0.462118)
# print(c)
 
# e为底的指数函数，20.085536923187668
# d = np.exp(3)
# print(d)
 
# 2的3次方，8
# f = np.power(2, 3)
# print(f)
 
# 点积，1*3+2*4=11
# g = np.dot([1, 2], [3, 4])
# print(g)
 
# 开方，5
# h = np.sqrt(25)
# print(h)
 
# 求和，10
# l = np.sum([1, 2, 3, 4])
# print(l)
 
# 平均值，5.5
# m = np.mean([4, 5, 6, 7])
# print(m)
 
# 标准差，0.96824583655185426
# p = np.std([1, 2, 3, 2, 1, 3, 2, 0])
# print(p)





"""对于array，默认执行对位运算。
涉及到多个array的对位运算需要array的维度一致，
如果一个array的维度和另一个array的子维度一致，
则在没有对齐的维度上分别执行对位运算，
这种机制叫做广播（broadcasting），
言语解释比较难，还是看例子理解"""

# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(a)
# print("***************")
 
# b = np.array([
#     [1, 2, 3],
#     [1, 2, 3]
# ])
# print(b)
# print("-----------------------------")
 
'''
维度一样的array，对位计算
array([[2, 4, 6],
       [5, 7, 9]])
'''
# print(a + b)
 
'''
array([[0, 0, 0],
       [3, 3, 3]])
'''
# print(a - b)
 
'''
array([[ 1,  4,  9],
       [ 4, 10, 18]])
'''
# print(a * b)
 
'''
array([[1, 1, 1],
       [4, 2, 2]])
'''
# print(a / b)
 
'''
array([[ 1,  4,  9],
       [16, 25, 36]])
'''
# print(a ** 2)
 
'''
array([[  1,   4,  27],
       [  4,  25, 216]])
'''
# print(a ** b)
 



# c = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ])
# d = np.array([2, 2, 2])
# print(c)
# print("**********")
# print(d)
# print("---------------------")
 
'''
广播机制让计算的表达式保持简洁
d和c的每一行分别进行运算
array([[ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11],
       [12, 13, 14]])
'''
# print(c + d)
 
'''
array([[ 2,  4,  6],
       [ 8, 10, 12],
       [14, 16, 18],
       [20, 22, 24]])
'''
# print(c * d)
 
'''
1和c的每个元素分别进行运算
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])
'''
# print(c - 1)  # c - 1 也可以运算哦  不信试试







# 线性代数模块
"""在深度学习相关的数据处理和运算中，
线性代数模块（linalg）是最常用的之一。
结合numpy提供的基本函数，
可以对向量，矩阵，或是说多维张量进行一些基本的运算"""

# a = np.array([1, 7])
# print(a)
# print(np.linalg.norm(a))
 
# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(b)
# c = np.array([1, 0, 1])
# print(c)
 
# # 矩阵和向量之间的乘法
# np.dot(b, c)            		# array([ 4, 10, 16])
# np.dot(c, b.T)          		# array([ 4, 10, 16])
 
# np.trace(b)             		# 求矩阵的迹，15
# np.linalg.det(b)        		# 求矩阵的行列式值，0
# np.linalg.matrix_rank(b)	# 求矩阵的秩，2，不满秩，因为行与行之间等差
 
# d = np.array([
#     [2, 1],
#     [1, 2]
# ])
 
# '''
# 对正定矩阵求本征值和本征向量
# 本征值为u，array([ 3.,  1.])
# 本征向量构成的二维array为v，
# array([[ 0.70710678, -0.70710678],
#        [ 0.70710678,  0.70710678]])
# 是沿着45°方向
# eig()是一般情况的本征值分解，对于更常见的对称实数矩阵，
# eigh()更快且更稳定，不过输出的值的顺序和eig()是相反的
# '''
# u, v = np.linalg.eig(d)
 
# # Cholesky分解并重建
# l = np.linalg.cholesky(d)
 
# '''
# array([[ 2.,  1.],
#        [ 1.,  2.]])
# '''
# np.dot(l, l.T)
 
# e = np.array([
#     [1, 2],
#     [3, 4]
# ])
 
# # 对不镇定矩阵，进行SVD分解并重建
# U, s, V = np.linalg.svd(e)
 
# S = np.array([
#     [s[0], 0],
#     [0, s[1]]
# ])
 
# '''
# array([[ 1.,  2.],
#        [ 3.,  4.]])
# '''
# np.dot(U, np.dot(S, V))







# 随机模块
"""随机模块包含了随机数产生和统计分布相关的基本函数，
Python本身也有随机模块random，
不过功能更丰富，还是来看例子："""
import numpy.random as random
 
# 设置随机数种子
# random.seed(42)
 
# 产生一个1x3，[0,1)之间的浮点型随机数
# array([[ 0.37454012,  0.95071431,  0.73199394]])
# 后面的例子就不在注释中给出具体结果了
# print(random.rand(1, 3))
 
# 产生一个[0,1)之间的浮点型随机数
# print(random.random())
 
# 下边4个没有区别，都是按照指定大小产生[0,1)之间的浮点型随机数array，不Pythonic…
# print(random.random((3, 3)))
# print(random.sample((3, 3)))
# print(random.random_sample((3, 3)))
# print(random.ranf((3, 3)))
 
# 产生10个[1,6)之间的浮点型随机数
# print(5*random.random(10) + 1)
# print(random.uniform(1, 6, 10))
 
# 产生10个[1,6]之间的整型随机数
# print(random.uniform(1, 6, 10))
 
# 产生2x5的标准正态分布样本
# print(random.normal(size=(5, 2)))
 
# 产生5个，n=5，p=0.5的二项分布样本
# print(random.binomial(n=5, p=0.5, size=5))
 
# a = np.arange(10)
# print(a)
 
# # 从a中有回放的随机采样7个
# print(random.choice(a, 4)) # 并不随机 6 , 3 , 7 , 4 , ..
 
# 从a中无回放的随机采样7个
# print(random.choice(a, 7, replace=False)) # 并不随机 8 , 1 , 5 , 0 , 7 , 2 , 9
 
# 对a进行乱序并返回一个新的array
# b = random.permutation(a) # 重复运行会得到同一个结果
# print(b)
 
# # 对a进行in-place乱序
# random.shuffle(a) # 重复运行会得到同一个结果
# print(a)
 
# 生成一个长度为9的随机bytes序列并作为str返回
# '\x96\x9d\xd1?\xe6\x18\xbb\x9a\xec'
# print(random.bytes(9)) # 重复运行会得到同一个结果






"""随机模块可以很方便地让我们做一些快速模拟去验证一些结论。
比如来考虑一个非常违反直觉的概率题例子：一个选手去参加一个TV秀，
有三扇门，其中一扇门后有奖品，这扇门只有主持人知道。
选手先随机选一扇门，但并不打开，
主持人看到后，会打开其余两扇门中没有奖品的一扇门。
然后，主持人问选手，是否要改变一开始的选择？

这个问题的答案是应该改变一开始的选择。
在第一次选择的时候，选错的概率是2/3，选对的概率是1/3。
第一次选择之后，主持人相当于帮忙剔除了一个错误答案，
所以如果一开始选的是错的，这时候换掉就选对了；
而如果一开始就选对，则这时候换掉就错了。
根据以上，一开始选错的概率就是换掉之后选对的概率（2/3），
这个概率大于一开始就选对的概率（1/3），所以应该换。
虽然道理上是这样，但是还是有些绕，要是通过推理就是搞不明白怎么办，
没关系，用随机模拟就可以轻松得到答案："""

# # 做10000次实验
# n_tests = 10000

# # 生成每次实验的奖品所在的门的编号
# # 0表示第一扇门，1表示第二扇门，2表示第三扇门
# winning_doors = random.randint(0, 3, n_tests)

# # 记录如果换门的中奖次数
# change_mind_wins = 0

# # 记录如果坚持的中奖次数
# insist_wins = 0

# # winning_door就是获胜门的编号
# for winning_door in winning_doors:

#     # 随机挑了一扇门
#     first_try = random.randint(0, 3)
    
#     # 其他门的编号
#     remaining_choices = [i for i in range(3) if i != first_try]
  
#     # 没有奖品的门的编号，这个信息只有主持人知道
#     wrong_choices = [i for i in range(3) if i != winning_door]

#     # 一开始选择的门主持人没法打开，所以从主持人可以打开的门中剔除
#     if first_try in wrong_choices:
#         wrong_choices.remove(first_try)
    
#     # 这时wrong_choices变量就是主持人可以打开的门的编号
#     # 注意此时如果一开始选择正确，则可以打开的门是两扇，主持人随便开一扇门
#     # 如果一开始选到了空门，则主持人只能打开剩下一扇空门
#     screened_out = random.choice(wrong_choices)
#     remaining_choices.remove(screened_out)
    
#     # 所以虽然代码写了好些行，如果策略固定的话，
#     # 改变主意的获胜概率就是一开始选错的概率，是2/3
#     # 而坚持选择的获胜概率就是一开始就选对的概率，是1/3
    
#     # 现在除了一开始选择的编号，和主持人帮助剔除的错误编号，只剩下一扇门
#     # 如果要改变注意则这扇门就是最终的选择
#     changed_mind_try = remaining_choices[0]

#     # 结果揭晓，记录下来
#     change_mind_wins += 1 if changed_mind_try == winning_door else 0
#     insist_wins += 1 if first_try == winning_door else 0

# # 输出10000次测试的最终结果，和推导的结果差不多：
# # You win 6616 out of 10000 tests if you changed your mind
# # You win 3384 out of 10000 tests if you insist on the initial choice
# print(
#     'You win {1} out of {0} tests if you changed your mind\n'
#     'You win {2} out of {0} tests if you insist on the initial choice'.format(
#         n_tests, change_mind_wins, insist_wins
#         )
# )







"""Python的可视化包 – Matplotlib
Matplotlib是Python中最常用的可视化工具之一，
可以非常方便地创建海量类型地2D图表和一些基本的3D图表。
Matplotlib最早是为了可视化癫痫病人的脑皮层电图相关的信号而研发，
因为在函数的设计上参考了MATLAB，所以叫做Matplotlib。
Matplotlib首次发表于2007年，在开源和社区的推动下，
现在在基于Python的各个科学计算领域都得到了广泛应用。
Matplotlib的原作者John D. Hunter博士是一名神经生物学家，
2012年不幸因癌症去世，
感谢他创建了这样一个伟大的库。

安装Matplotlib的方式和numpy很像，
可以直接通过Unix/Linux的软件管理工具，
比如Ubuntu 16.04 LTS下，输入：

>> sudo apt install python-matplotlib

或者通过pip安装：

>> pip install matplotlib

Windows下也可以通过pip，或是到官网下载：
https://matplotlib.org/

Matplotlib非常强大，
不过在深度学习中常用的其实只有很基础的一些功能，
这节主要介绍2D图表，3D图表和图像显示。
"""




"""Matplotlib中最基础的模块是pyplot。
先从最简单的点图和线图开始，
比如我们有一组数据，还有一个拟合模型，
通过下面的代码图来可视化"""
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# # 通过rcParams设置全局横纵轴字体大小
# mpl.rcParams['xtick.labelsize'] = 24
# mpl.rcParams['ytick.labelsize'] = 24

# np.random.seed(42)

# # x轴的采样点
# x = np.linspace(0, 5, 100)

# # 通过下面曲线加上噪声生成数据，所以拟合模型就用y了……
# y = 2*np.sin(x) + 0.3*x**2
# y_data = y + np.random.normal(scale=0.3, size=100)

# # figure()指定图表名称
# plt.figure('data')

# # '.'标明画散点图，每个散点的形状是个圆
# plt.plot(x, y_data, '.')

# # 画模型的图，plot函数默认画连线图
# plt.figure('model')
# plt.plot(x, y)

# # 两个图画一起
# plt.figure('data & model')

# # 通过'k'指定线的颜色，lw指定线的宽度
# # 第三个参数除了颜色也可以指定线形，比如'r--'表示红色虚线
# # 更多属性可以参考官网：http://matplotlib.org/api/pyplot_api.html
# plt.plot(x, y, 'k', lw=3)

# # scatter可以更容易地生成散点图
# plt.scatter(x, y_data)

# # 将当前figure的图保存到文件result.png
# plt.savefig('result.png')

# # 一定要加上这句才能让画好的图显示在屏幕上
# plt.show()





"""点和线图表只是最基本的用法，
有的时候我们获取了分组数据要做对比，
柱状或饼状类型的图或许更合适"""

"""在这段代码中又出现了一个新的东西叫做，
一个用ax命名的对象。
在Matplotlib中，画图时有两个常用概念，
一个是平时画图蹦出的一个窗口，这叫一个figure。
Figure相当于一个大的画布，在每个figure中，
又可以存在多个子图，这种子图叫做axes。
顾名思义，有了横纵轴就是一幅简单的图表。
在下面代码中，先把figure定义成了一个一行两列的大画布，
然后通过fig.add_subplot()加入两个新的子图。
subplot的定义格式很有趣，
数字的前两位分别定义行数和列数，
最后一位定义新加入子图的所处顺序，
当然想写明确些也没问题，用逗号分开即可"""
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# mpl.rcParams['axes.titlesize'] = 20
# mpl.rcParams['xtick.labelsize'] = 16
# mpl.rcParams['ytick.labelsize'] = 16
# mpl.rcParams['axes.labelsize'] = 16
# mpl.rcParams['xtick.major.size'] = 0
# mpl.rcParams['ytick.major.size'] = 0

# # 包含了狗，猫和猎豹的最高奔跑速度，还有对应的可视化颜色
# speed_map = {
#     'dog': (48, '#7199cf'),
#     'cat': (45, '#4fc4aa'),
#     'cheetah': (120, '#e1a7a2')
# }

# # 整体图的标题
# fig = plt.figure('Bar chart & Pie chart')

# # 在整张图上加入一个子图，121的意思是在一个1行2列的子图中的第一张
# ax = fig.add_subplot(121)
# ax.set_title('Running speed - bar chart')

# # 生成x轴每个元素的位置
# xticks = np.arange(3)

# # 定义柱状图每个柱的宽度
# bar_width = 0.5

# # 动物名称
# animals = speed_map.keys()

# # 奔跑速度
# speeds = [x[0] for x in speed_map.values()]

# # 对应颜色
# colors = [x[1] for x in speed_map.values()]

# # 画柱状图，横轴是动物标签的位置，纵轴是速度，定义柱的宽度，同时设置柱的边缘为透明
# bars = ax.bar(xticks, speeds, width=bar_width, edgecolor='none')

# # 设置y轴的标题
# ax.set_ylabel('Speed(km/h)')

# # x轴每个标签的具体位置，设置为每个柱的中央
# ax.set_xticks(xticks+bar_width/2)

# # 设置每个标签的名字
# ax.set_xticklabels(animals)

# # 设置x轴的范围
# ax.set_xlim([bar_width/2-0.5, 3-bar_width/2])

# # 设置y轴的范围
# ax.set_ylim([0, 125])

# # 给每个bar分配指定的颜色
# for bar, color in zip(bars, colors):
#     bar.set_color(color)

# # 在122位置加入新的图
# ax = fig.add_subplot(122)
# ax.set_title('Running speed - pie chart')

# # 生成同时包含名称和速度的标签
# labels = ['{}\n{} km/h'.format(animal, speed) for animal, speed in zip(animals, speeds)]

# # 画饼状图，并指定标签和对应颜色
# ax.pie(speeds, labels=labels, colors=colors)

# plt.show()




"""3D的散点图也是常常用来查看空间样本分布的一种手段，
并且画起来比表面图和网线图更加简单，来看例子"""

"""下面例子中，为了方便，直接先采样了一堆3维的正态分布样本，
保证方向上的均匀性。然后归一化，让每个样本到原点的距离为1，
相当于得到了一个均匀分布在球面上的样本。
再接着把每个样本都乘上一个均匀分布随机数的开3次方，
这样就得到了在球体内均匀分布的样本，
最后根据判别平面3x+2y-z-1=0对平面两侧样本用不同的形状和颜色画出."""

# import matplotlib.pyplot as plt
# import numpy as np

# from mpl_toolkits.mplot3d import Axes3D

# np.random.seed(42)

# # 采样个数500
# n_samples = 500
# dim = 3

# # 先生成一组3维正态分布数据，数据方向完全随机
# samples = np.random.multivariate_normal(
#     np.zeros(dim),
#     np.eye(dim),
#     n_samples
# )

# # 通过把每个样本到原点距离和均匀分布吻合得到球体内均匀分布的样本
# for i in range(samples.shape[0]):
#     r = np.power(np.random.random(), 1.0/3.0)
#     samples[i] *= r / np.linalg.norm(samples[i])

# upper_samples = []
# lower_samples = []

# for x, y, z in samples:
#     # 3x+2y-z=1作为判别平面
#     if z > 3*x + 2*y - 1:
#         upper_samples.append((x, y, z))
#     else:
#         lower_samples.append((x, y, z))

# fig = plt.figure('3D scatter plot')
# ax = fig.add_subplot(111, projection='3d')

# uppers = np.array(upper_samples)
# lowers = np.array(lower_samples)

# # 用不同颜色不同形状的图标表示平面上下的样本
# # 判别平面上半部分为红色圆点，下半部分为绿色三角
# ax.scatter(uppers[:, 0], uppers[:, 1], uppers[:, 2], c='r', marker='o')
# ax.scatter(lowers[:, 0], lowers[:, 1], lowers[:, 2], c='g', marker='^')

# plt.show()



# 显示图片
# import matplotlib.pyplot as plt
 
# # 读取一张小白狗的照片并显示
# plt.figure('刘亦菲')
# little_dog_img = plt.imread('liuyifei.jpg')
# plt.imshow(little_dog_img)
 
# Z是上小节生成的随机图案，img0就是Z，img1是Z做了个简单的变换
# img0 = Z
# img1 = 3*Z + 4
 
# cmap指定为'gray'用来显示灰度图
# fig = plt.figure('Auto Normalized Visualization')
# ax0 = fig.add_subplot(121)
# ax0.imshow(little_dog_img, cmap='gray')
 
# ax1 = fig.add_subplot(122)
# ax1.imshow(little_dog_img, cmap='gray')
 
# plt.show()








