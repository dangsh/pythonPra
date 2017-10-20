year = 1898
month = 9
day = 2

days = 0

months = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(12):
	if i < month - 1:
		# print(months[i])
		days = days + months[i] 

print(days + day)