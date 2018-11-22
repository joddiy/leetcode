# -*- coding: utf-8 -*-
# file: productExceptSelf.py
# author: joddiyzhang@gmail.com
# time: 2018/11/22 8:41 PM
# ------------------------------------------------------------------------

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            nums[i] = left[i] * right[i]

        return nums

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        p = 1
        for i in range(n):
            res[i] = p
            p *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
