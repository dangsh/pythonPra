import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1 , 3 , 5 , np.nan , 6 , 8])
# print(s)


dates = pd.date_range('20130101' , periods = 6);
# print(dates)


# # 通过numpy array 创建 DataFrame
df = pd.DataFrame(np.random.randn(6 , 4) , index = dates , columns=list('ABCD'));
# print(df);

# # 通过 dict obj 来创建 DataFrame  
# df2 = pd.DataFrame({
#     'A' : 1. , 
#     'B' : pd.Timestamp('20130102') ,
#     'C' : pd.Series(1 , index=list(range(4)) , dtype='float32') ,
#     'D' : np.array([3] * 4 , dtype='int32') , 
#     'E' : pd.Categorical(['test' , 'train' , 'test' , 'train'])  , 
#     'F' : 'foo'
# });
# print(df2);
# 拥有特殊的数据类型
# print(df2.dtypes);


# 查看数据
print(df);
# # 参数可有可无 没有的话,代表前/后 5条
print(df.head(3));
print("-----")
print(df.tail(1));

# 显示索引,列,和底层的numpy数据
# print(df);
# print(df.index); # 行号
# print(df.columns); # 列号
# print(df.values); # values 二维数组的方式展示

# describe()  对数据的快速统计汇总
# print(df);
# print(df.describe());

# 数据转置
# print(df);
# print(df.T);

# 按轴进行排序
# print(df);
# print(df.sort_index(axis=1 , ascending=False)); # 0 行号  1 列号

# 按值排序
# print(df);
# print(df.sort_values(by='B' , ascending=False)); # 默认是升序

# 获取一列或一行数据
# print(df);
# # print(df["A"]); # 或者 print(df.A);
# # print(df[0:2]); # df[0:1] df[0:2] 如果只获取一行数据的时候,不能写成df[0] 要写成df[0:1]
# # 也可以用一下方式来获取
# print(df['20130102':'20130104']);  # 但不要这样写 df["20130102"]
# # 如果只想获取一行,可以这样写: df["20130102":"20130102"]


# 通过标签获取交叉数据
# print(df)
# print(df.loc[dates[0]]); # 相当于 print(df["20130101":"20130101"])
# 只获取A , B 两列数据
# print(df.loc[: , ["A" , "B"]])  # 注意 ":," 一定不能少
# 从第二行到第四行,并且 只有A , B 两列的数据
# print(df.loc['20130102':'20130104',['A','B']])
# 获取第一行的且只有A , B 两列数据
# print(df.loc['20130101',['A','B']])
# 获取一个标量
# print(df.loc[dates[0],'A'])
# 快速访问一个标量,与上面方法等价
# print(df.at[dates[0],'A'])


# 通过位置进行选择
# 通过传递数值进行位置选择（选择的是行)
# print(df)
# print(df.iloc[3])
# 通过数值进行切片，与numpy/python中的情况类似
# print(df.iloc[3:5,1:3])
# 通过指定一个位置的列表，与numpy/python中的情况类似
# print(df.iloc[[1,2,4],[0,2]])
# 对行进行切片
# print(df.iloc[1:3,:])
# 对列进行切片
# print(df.iloc[:,1:3])
# 获取特定的值
# print(df.iloc[1,1])
# print(df.iat[1,1])


# 布尔索引
# print(df)
# 使用一个单独列的值来选择数据：
# print(df[df.A > 0])
# 使用where操作来选择数据：
# print(df[df > 0])
# 使用isin()方法来过滤
# df2 = df.copy()
# df2['E'] = ['one', 'one','two','three','four','three']
# print(df2)
# print(df2[df2['E'].isin(['two','four'])])



#  设置
# print(df)
# 设置一个新的列
# s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
# print(s1)
# print(df)
# df['F'] = s1
# print(df)
# 通过标签设置新的值
# df.at[dates[0],'A'] = 0
# print(df)
#  通过位置设置新的值：
# df.iat[0,1] = 0
# print(df)
# 通过一个numpy数组设置一组新值：
# df.loc[:,'D'] = np.array([5] * len(df))
# print(df)
# 通过where操作来设置新的值：
# df2 = df.copy()
# df2[df2 > 0] = -df2
# print(df2)


# 缺失值处理(会返回新的结果)
# 在pandas中，使用np.nan来代替缺失值，这些值将默认不会包含在计算中
# reindex()方法可以对指定轴上的索引进行改变/增加/删除操作，这将返回原始数据的一个拷贝：
# df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# print(df1)
# df1.loc[dates[0]:dates[1],'E'] = 1
# print(df1)
# 去掉包含缺失值的行：
# print(df1.dropna(how='any'))
# print(df1)
# 对缺失值进行填充：
# print(df1.fillna(value=5))
# print(df1)
# 对数据进行布尔填充：
# print(pd.isna(df1))




# 相关操作
# 统计（相关操作通常情况下不包括缺失值）
# print(df)
# 执行描述性统计
# print(df.mean())
# 在其他轴上进行相同的操作：
# print(df.mean(1))
# 对于拥有不同维度，需要对齐的对象进行操作。Pandas会自动的沿着指定的维度进行广播：
# s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
# print(s)
# print(df.sub(s, axis='index'))


# 应用
# print(df)
# 对数据应用函数
# print(df.apply(np.cumsum))
# print(df.apply(lambda x: x.max() - x.min()))
# 直方图
# s = pd.Series(np.random.randint(0, 7, size=10))
# print(s)
# print(s.value_counts())


# 字符串方法
# Series对象在其str属性中配备了一组字符串处理方法，可以很容易的应用到数组中的每个元素，如下段代码所示
# s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
# print(s)
# print(s.str.lower())



#   合并
# Pandas提供了大量的方法能够轻松的对Series，DataFrame和Panel对象进行各种符合各种逻辑关系的合并操作
# Concat
# df = pd.DataFrame(np.random.randn(10, 4))
# print(df)
# pieces = [df[:3], df[3:7], df[7:]]
# print(pd.concat(pieces))
# Join 类似于SQL类型的合并
# left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
# right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
# print(left)
# print(right)
# print(pd.merge(left, right, on='key'))

# Append 将一行连接到一个DataFrame上
# df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
# print(df)
# s = df.iloc[3]
# print(s)
# print(df.append(s, ignore_index=True))




# 分组
# 对于”group by”操作，我们通常是指以下一个或多个操作步骤：

#  （Splitting）按照一些规则将数据分为不同的组；

#  （Applying）对于每组数据分别执行一个函数；

#  （Combining）将结果组合到一个数据结构中；
# df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
#                          'foo', 'bar', 'foo', 'foo'],
#                    'B' : ['one', 'one', 'two', 'three',
#                           'two', 'two', 'one', 'three'],
#                     'C' : np.random.randn(8),
#                     'D' : np.random.randn(8)})
# print(df)

# 分组并对每个分组执行sum函数
# print(df.groupby('A').sum())

# 通过多个列进行分组形成一个层次索引，然后执行函数：
# print(df.groupby(['A','B']).sum())




# Reshaping
# Stack
# tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
#                       'foo', 'foo', 'qux', 'qux'],
#                     ['one', 'two', 'one', 'two',
#                       'one', 'two', 'one', 'two']]))
                      
# print(tuples)
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# df2 = df[:4]
# # print(df2)

# stacked = df2.stack()
# print(stacked)

# print(stacked.unstack())
# print(stacked.unstack(1))
# print(stacked.unstack(0))


# 数据透视表
# df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
#                    'B' : ['A', 'B', 'C'] * 4,
#                    'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
#                      'D' : np.random.randn(12),
#                     'E' : np.random.randn(12)})
# print(df)

# # 可以从这个数据中轻松的生成数据透视表
# print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))




# 时间序列
# Pandas在对频率转换进行重新采样时拥有简单、强大且高效的功能
# （如将按秒采样的数据转换为按5分钟为单位进行采样的数据）。这种操作在金融领域非常常见
# rng = pd.date_range('1/1/2012', periods=100, freq='S')
# ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
# print(ts.resample('5Min').sum())

# 时区表示
# rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
# ts = pd.Series(np.random.randn(len(rng)), rng)
# print(ts)
# ts_utc = ts.tz_localize('UTC')
# print(ts_utc)

# 时区转换
# print(ts_utc.tz_convert('US/Eastern'))

# 时间跨度转换
# rng = pd.date_range('1/1/2012', periods=5, freq='M')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts)
# ps = ts.to_period()
# print(ps)
# print(ps.to_timestamp())



# 时期和时间戳之间的转换使得可以使用一些方便的算术函数
# prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
# ts = pd.Series(np.random.randn(len(prng)), prng)
# ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
# print(ts.head())




# Categorical
# 从0.15版本开始，pandas可以在DataFrame中支持Categorical类型的数据
# df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
# df["grade"] = df["raw_grade"].astype("category")
# print(df["grade"])

# 将Categorical类型数据重命名为更有意义的名称：
# df["grade"].cat.categories = ["very good", "good", "very bad"]

# 对类别进行重新排序，增加缺失的类别
# df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
# print(df["grade"])

# 排序是按照Categorical的顺序进行的而不是按照字典顺序进行
# print(df.sort_values(by="grade"))

# # 对Categorical列进行排序时存在空的类别
# print(df.groupby("grade").size())


# 画图
# 具体请参考文档
# http://pandas.pydata.org/pandas-docs/stable/visualization.html#visualization
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# # # print(ts)
# print(ts.plot())




# from matplotlib.font_manager import FontProperties 

# font = FontProperties(fname=r"./simsun/simsun.ttc", size=14) 

# df = pd.DataFrame({"山东省": [3872.18, 5960.42, 6650.02, 7162.2, 7662.1, 8542.44] , 
#             "江苏省": [4057.39, 6004.21, 6680.34, 7199.95, 7697.82, 8582.727627]},
#             index=["1995年", "1996年", "1997年", "1998年", "1999年", "2000年"])

# ax = df.plot(color=["g", "r"],style=["--","-"], title=u"山东江苏GDP(单位:亿元)")

# # 加上下面两行  让中文显示
# labels = ax.get_xticklabels()+ax.legend().texts+[ax.title]
# for label in labels : 
#     label.set_fontproperties(font) 

    
# plt.show()

# # 对于DataFrame来说，plot是一种将所有列及其标签进行绘制的简便方法
# df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
#                    columns=['A', 'B', 'C', 'D'])
# df = df.cumsum()
# plt.figure(); df.plot(); plt.legend(loc='best')





# 导入和保存数据
# 写入csv文件
# df.to_csv('foo.csv')

# 从csv文件中读取
# print(pd.read_csv('foo.csv'))


# 写入HDF5存储 缺少模块
# df.to_hdf('foo.h5','df')
# 从HDF5存储中读取
# print(pd.read_hdf('foo.h5','df'))

# 写入excel文件 缺少模块
# df.to_excel('foo.xlsx', sheet_name='Sheet1')
# 从excel文件中读取
# print(pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']))




# pandas cookBook
# idioms 习语 习惯用法
# df = pd.DataFrame(
#      {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
# print(df)

# An if-then on one column
# df.loc[df.AAA >= 5,'BBB'] = -1;
# print(df)

# An if-then with assignment to 2 columns
# df.loc[df.AAA >= 5,['BBB','CCC']] = 555;
# print(df)

# Add another line with different logic, to do the -else
# df.loc[df.AAA < 5,['BBB','CCC']] = 2000;
# print(df)

# Or use pandas where after you’ve set up a mask
# df_mask = pd.DataFrame({'AAA' : [True] * 4, 'BBB' : [False] * 4,'CCC' : [True,False] * 2})
# print(df_mask)
# print(df.where(df_mask,-1000))




# 绘图操作
# 参考地址
# http://pandas.pydata.org/pandas-docs/stable/visualization.html
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# df = pd.DataFrame(
#      {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
# df = df.cumsum()
# print(df)
# # df.plot()
# # df.plot(kind="bar")kde  box barh area density hist line 

# df.plot(kind="area")

#  点

# df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])

# df.plot.scatter(x='a', y='b');

# ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1');
# df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax);

# df.plot.scatter(x='a', y='b', c='c', s=50);

# df.plot.scatter(x='a', y='b', s=df['c']*200);

# matplotlib 官网案例
# https://matplotlib.org/gallery.html

# df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])

# df['b'] = df['b'] + np.arange(1000)

# df.plot.hexbin(x='a', y='b', gridsize=25)

# plt.show()





