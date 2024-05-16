import sys

from tools import *
import pprint


class Solution(object):

    # @print_
    # def productExceptSelf(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     nums = [1] + nums + [1]
    #     left = [1] * len(nums)
    #     right = [1] * len(nums)
    #     for i in range(1, len(nums) - 1):
    #         left[i] = left[i - 1] * nums[i]
    #     for i in range(len(nums) - 2, 0, -1):
    #         right[i] = right[i + 1] * nums[i]
    #     ret = []
    #     for i in range(1, len(nums) - 1):
    #         ret.append(left[i - 1] * right[i + 1])
    #     return ret

    @print_
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = [1] * len(nums)
        p = 1
        for i in range(len(dp)):
            dp[i] *= p
            p *= nums[i]
        p = 1
        for i in range(len(dp) - 1, -1, -1):
            dp[i] *= p
            p *= nums[i]
        return dp


solution = Solution().productExceptSelf
solution(nums=[1, 2, 3, 4])
# solution(nums=[-1, 1, 0, -3, 3])
