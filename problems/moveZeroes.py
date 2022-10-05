from tools import *


class Solution(object):
    @print_
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        i = 0
        # find the first zero
        while i < n and nums[i] != 0:
            i += 1
        j = i
        while True:
            # find the first non zero
            while j < n and nums[j] == 0:
                j += 1
            if j >= n:
                break
            else:
                # swap
                nums[i], nums[j] = nums[j], nums[i]
                # if next of j is 0, then i += 1
                # else, we first swap this zero to next, so still can i += 1
                i += 1
        return nums

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        i = 0
        # i is the fist zero
        while i < n and nums[i] != 0:
            i += 1
        for j in range(i + 1, n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

solution = Solution().moveZeroes

solution([0, 1, 0, 3, 12])
solution([1, 0, 1])
