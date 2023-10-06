import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        all_sum = sum(nums)

        max_ending_here = 0
        max_so_sar = -sys.maxsize
        for i in range(len(nums)):
            max_ending_here += nums[i]
            max_so_sar = max(max_ending_here, max_so_sar)
            max_ending_here = max(max_ending_here, 0)

        min_ending_here = 0
        min_so_sar = sys.maxsize
        for i in range(len(nums)):
            min_ending_here += nums[i]
            min_so_sar = min(min_ending_here, min_so_sar)
            min_ending_here = min(min_ending_here, 0)

        if max_so_sar < 0:
            return max_so_sar
        else:
            return max(max_so_sar, all_sum - min_so_sar)


solution = Solution().maxSubarraySumCircular
solution(nums=[1, -2, 3, -2])
solution(nums=[5, -3, 5])
solution(nums=[-3, -2, -3])
