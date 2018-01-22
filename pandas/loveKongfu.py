import numpy as np 

#[动作镜头数 ， 爱情镜头数]
dataArr = np.array([[1 , 100] , [45 , 123] , [143 , 23] , [116 , 8]])
labels = ["爱情片" , "爱情片" , "动作片" , "动作片"]

#准备 KNN 算法
"""testData:测试数据（测试集） 
dataSet:用于训练的数据（样本集，训练集）
label：分类的标签
k：KNN算法中，算法参数，选择距离最小的k个点"""
def KNNClassify(testData , dataSet , labels , k):
    dataHang = dataSet.shape[0]
    #在 列向量方向上，重复testData共 dataHang 次 
    #在 行向量方向上，重复testData共 一 次
    #将一盒测试数据重复4行一列 -----》 跟样本集是一样的矩阵结构

    xiangLiangJvzhen = np.tile(testData , (dataHang , 1) ) - dataSet
    xiangLiangJvzhenPingfang = xiangLiangJvzhen ** 2
    XYqiuhe = xiangLiangJvzhenPingfang.sum(axis = 1)
    distance = XYqiuhe ** 0.5
    sortDistance = distance.argsort()
    print(distance)
    print(sortDistance)
    #准备一个字典{} 用来记录类别出现的次数
    leibieCount = {}
    for i in range(k):
        xiabiao = sortDistance[i]
        leibie = labels[xiabiao]
        leibieCount[leibie] = leibieCount.get(leibie , 0) + 1 
    print(leibieCount)
    aiqingCount = leibieCount["爱情片"]
    dongzuoCount = leibieCount["动作片"]
    if aiqingCount > dongzuoCount:
        return "爱情片"
    else :
        return "动作片"
testMovie = [333 , 22]
result = KNNClassify(testMovie , dataArr , labels , 3)
print("经过分析， 该电影是：：：：" + result)