import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


solution = Solution().lengthOfLIS
solution(nums=[10, 9, 2, 5, 3, 7, 101, 18])
solution(nums=[0, 1, 0, 3, 2, 3])
solution(nums=[7, 7, 7, 7, 7, 7, 7])
