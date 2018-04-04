"""
//
//                       _oo0oo_
//                      o8888888o
//                      88" . "88
//                      (| -_- |)
//                      0\  =  /0
//                    ___/`---'\___
//                  .' \\|     |// '.
//                 / \\|||  :  |||// \
//                / _||||| -:- |||||- \
//               |   | \\\  -  /// |   |
//               | \_|  ''\---/''  |_/ |
//               \  .-\__  '-'  ___/-. /
//             ___'. .'  /--.--\  `. .'___
//          ."" '<  `.___\_<|>_/___.' >' "".
//         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
//         \  \ `_.   \_ __\ /__ _/   .-` /  /
//     =====`-.____`.___ \_____/___.-`___.-'=====
//                       `=---='
//
//
//     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//               佛祖保佑         永无BUG
//
//
//
"""

# #二分查找
# def get(list , num):
# 	min = 0 
# 	max = len(list) - 1
# 	while min <= max:
# 		guess = (min + max)//2
# 		if list[guess] == num:
# 			return guess
# 		elif list[guess] > num:
# 			max = guess - 1
# 		else:
# 			min = guess + 1
# 	return None

# if __name__ == "__main__":
# 	list = [1 , 2 , 4 , 6 , 7 , 8]
# 	print(get(list , 17))

# #查找最小值
# def get_min(list):
# 	min = 0
# 	for i in range(len(list)):
# 		if list[i] <= list[min]:
# 			min = i
# 	return min

# list = [5 , 2 , 4 , 6 , 1 , 8 , 10]
# #排序
# new_arr = []
# for i in range(len(list)):
# 	a = get_min(list)
# 	new_arr.append(list[a])
# 	list.pop(a)
# print(new_arr)

# 递归求和
# def sum(list):
# 	if list == []:
# 		return 0
# 	return list[0] + sum(list[1:])

# def sum(list):
# 	if len(list) == 0:
# 		return 0
# 	return list[0] + sum(list[1:])

# def sum(list):
# 	if len(list) == 1:
# 		return list[0]
# 	return list[0] + sum(list[1:])

# print(sum([1,2,3,4,5,6]))

# 递归计数
# def count(list):
# 	if list == []:
# 		return 0
# 	return 1 + count(list[1:])

# print(count([1,2,3,4,5,6]))

# 递归求最大
# def max(list):
# 	if len(list) == 2:
# 		return list[0] if list[0] > list[1] else list[1]
# 	sub_max = max(list[1:])
# 	return list[0] if list[0] > sub_max else sub_max	

# print(max([1,4,2,3]))

# 递归快速排序
# def quicksort(array):
# 	if len(array) < 2:
# 		return array
# 	else:
# 		pivot = array[0]
# 		less = [i for i in array[1:] if i <= pivot]
# 		greater = [i for i in array[1:] if i > pivot]
# 		return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([1,4,1,2,8,5,7]))		