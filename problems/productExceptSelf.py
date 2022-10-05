from tools import *


class Solution(object):
    @print_
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = [1] * len(nums)
        p = 1
        for i in range(len(nums)):
            dp[i] *= p
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            dp[i] *= p
            p *= nums[i]
        return dp


solution = Solution().productExceptSelf

solution([1, 2, 3, 4])
