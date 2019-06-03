# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 下午2:35
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows


class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, j in enumerate(nums):
            num_dict[j] = i
        for k, v in enumerate(nums):
            need_num = target - v
            if need_num in num_dict and num_dict[need_num] != k:
                return num_dict[need_num] , k

class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        num_dict = {j:i for i,j in enumerate(nums)}
        for i in nums:
            need_num = target - i
            if need_num in num_dict and num_dict[need_num] != nums.index(i):
                return num_dict[need_num] , nums.index(i)

class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, j in enumerate(nums):
            print(num_dict)
            need_num = target - j
            if need_num in num_dict and num_dict[need_num] != i:
                return num_dict[need_num] , i
            num_dict[j] = i




nums = [3,3]
target = 6
print Solution().twoSum(nums , target)