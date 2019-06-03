# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 下午2:35
# @Magician  : Dangsh
# When I wrote this , only God and I understood what I was doing
# Now , God only knows


class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, j in enumerate(nums):
            num_dict["j"] = i

        print num_dict
        for k, v in enumerate(nums):
            tmp = target - v
            if tmp in num_dict and i != k:
                return i, k

