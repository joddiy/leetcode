# -*- coding: utf-8 -*-
# file: twoSum.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 1:24 PM
# ------------------------------------------------------------------------

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_table and hash_table[diff] != i:
                return [i, hash_table[diff]]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_table and hash_table[diff] != i:
                return [hash_table[diff], i]
            hash_table[nums[i]] = i


print(Solution().twoSum([3, 3], 6))
