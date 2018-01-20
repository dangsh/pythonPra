import numpy as np
import matplotlib.pyplot as plt

#读数据
x , y = [] , []
with open('fangziData.txt' , encoding='utf-8') as f:
    for line in f.readlines():
        x.append(line.split(',')[0])
        y.append(line.split(',')[1])
f.close()


#绘制到界面上
plt.scatter(x , y , edgecolors='green' , alpha='0.6')
plt.show()
