import pandas
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties 

font = FontProperties(fname=r"./simsun/simsun.ttc", size=14) 
content = pandas.read_table('hailunYuehuiData.txt' , sep="\t")
newSeries = content["喜欢程度"].replace(['didntLike' , 'smallDoses' , 'largeDoses'],[1 , 2 , 3])
content["喜欢程度"] = newSeries
# print(content)

xinlai = pandas.DataFrame()
xinlai['x'] = pandas.Series([13.276369])
xinlai['y'] = pandas.Series([42667])
print(xinlai)

didntlike = content[content['喜欢程度'].isin([1])]
midlike = content[content['喜欢程度'].isin([2])]
largelike = content[content['喜欢程度'].isin([3])]

ax = didntlike.plot.scatter(x='娱乐时间' , y='飞行时间' , color='pink' , label='不喜欢')
ax = midlike.plot.scatter(x='娱乐时间' , y='飞行时间' , color='green' , label='一般喜欢' , ax = ax)
ax = largelike.plot.scatter(x='娱乐时间' , y='飞行时间' , color='yellow' , label='很喜欢' , ax = ax)
xinlai.plot.scatter(x='x' , y='y'  , color='black' , label='新来的' , ax = ax)

plt.legend(loc="best")
labels = ax.get_xticklabels()+ax.legend().texts+[ax.title]
for label in labels : 
    label.set_fontproperties(font) 

plt.xlabel(u'娱乐时间' , fontproperties = font)
plt.ylabel(u'飞行时间' , fontproperties = font)
plt.show()


