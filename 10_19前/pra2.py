a = [2,1,6,4,9]
b = [3,7,5,8,11,10]
c = []


# [3, 5, 7, 8, 10, 11]
a.sort()

# a            [1, 2, 4, 6, 9]
for j in range(len(a)-1):
	for i in range(len(b)-1):
		if b[i]>a[j] and b[i]<a[j+1]:
			

