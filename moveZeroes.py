# -*- coding: utf-8 -*-
# file: moveZeroes.py
# author: joddiyzhang@gmail.com
# time: 2018/11/20 7:36 PM
# ------------------------------------------------------------------------

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_of_zero = 0
        for i in range(len(nums)):

            if nums[i] == 0:
                num_of_zero += 1
            else:
                nums[i - num_of_zero], nums[i] = nums[i], nums[i - num_of_zero]
        return nums

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1  # only when replace, add one, this zero records the first zero


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
