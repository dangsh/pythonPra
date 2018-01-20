import numpy as np
import matplotlib.pyplot as plt

# 读数据
x , y , z = [] , [] , []
with open('people.txt' , encoding='utf-8') as f:
    for line in f.readlines():
        x.append(int(line.split(' ')[1])) #year
        y.append(int(line.split(' ')[2])) #boy
        z.append(int(line.split(' ')[3].replace('\n' , ''))) #girl
    print(x , y , z)
f.close()

c = [1,2,3]
p = [4,5,6]
# #绘制到界面上
plt.stackplot(x , y , z , labels=[1,2,3])
plt.show()
