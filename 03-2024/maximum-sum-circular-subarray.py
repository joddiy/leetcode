import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        j = 0
        max_ = -sys.maxsize
        cur = 0
        while j < n:
            cur += nums[j]
            max_ = max(max_, cur)
            if cur <= 0:
                cur = 0
            j += 1

        j = 0
        min_ = sys.maxsize
        cur = 0
        while j < n:
            cur += nums[j]
            min_ = min(min_, cur)
            if cur >= 0:
                cur = 0
            j += 1

        if max_ < 0:
            return max_
        else:
            return max(max_, sum(nums) - min_)


solution = Solution().maxSubarraySumCircular
solution(nums=[1, -2, 3, -2])
solution(nums=[5, -3, 5])
solution(nums=[-3, -2, -3])
