import numpy as np

#多维数组 numpy.array 将python中的 tuple 数据做成一维数组
# a = [[1 , 2 , 3 , 4],[5 , 6 , 7 , 8]]
# a = np.array(a)
# print(a)

# print(np.array(((1 , 3 , 5 , 7),(1 , 3 , 5 , 7))))

# a = np.array([1 , 2 , 3] , dtype=np.string_)
# print(a)

# print(a.astype(float))


# a = np.array(((1 , 2 , 3) , (4 , 6 , 6)))
# print(a)
# print(a[0])
# print(a[1][1])
# print(a[:,0])

arr = []
def getData():
    with open('fangziData.txt' , encoding='utf-8') as f:
        for line in f.readlines():
            arr.append(line.split(','))
        num = np.array(arr , dtype=np.int)
    f.close()
    return num 

data = getData()

# print(data)
'''改变temp会改变data ， 所以可推断temp ， x 指向同一块内存空间'''
# temp = data[:,1]
# print(temp)
# temp[0] = 10
# print(temp)
# print(data)


arr = np.arange(10)
print(arr)
print(type(arr))
print(arr[4])
print(arr[3:6])
arr[3:6] = 12
print(arr)
