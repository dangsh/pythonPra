str1 = 'abcd12345ed125ss123058789'

## 方法2
import re
reg = '.*?(\d+).*?'
a = re.findall(reg , str1)
max = len(a[0])
maxdata = a[0]

for i in a:
	if len(i) > max:
		max = len(i)
		maxdata = i
print(max , maxdata)

## 方法1

# i = 0
# length = 0
# maxlen = 0
# index = 0
# for k,v in enumerate(str1):
# 	try:
# 		v = int(v)
# 	except:
# 		pass
# 	if type(v) == int:
# 		while True:
# 			num = ''
# 			try:
# 				num = str1[k+i]
# 			except:
# 				pass
# 			if num and num in '1234567890':
# 				length += 1
# 				i += 1
# 			else:
# 				i = 0
# 				if length > maxlen:
# 					maxlen = length
# 					index = k
# 				length = 0
# 				break
# print(str1[index:index+16] , maxlen)
