#取最小值排序
a = [2,5,1,7,3,9,4]

for i in range(len(a) - 1):
	minIndex = i;
	currentIndex = i;
	min = a[i];

	for xiaBiao,zhi in enumerate(a):
		if xiaBiao < i:
			continue;

		if zhi < min:
			min = zhi;
			currentIndex =xiaBiao;


	if minIndex != currentIndex:
		temp = a[minIndex];
		a[minIndex] = a[currentIndex];
		a[currentIndex] = temp;

print(a)