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


def getData():
    with open('fangziData.txt' , encoding='utf-8') as f:
        for i in range(47):
            line = f.readline()
            print(line)
    f.close()


getData()