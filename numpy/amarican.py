import pandas
import matplotlib.pyplot as plt

urlStr = "http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt"
content = pandas.read_table(urlStr , sep=" ")
content2 = content.set_index("year")


content.boys.plot(color='#ff00ff')
content.girls.plot(color='#00ff00')
plt.legend(loc="best")
plt.show()

# content2.plot(color='b')
# plt.show()