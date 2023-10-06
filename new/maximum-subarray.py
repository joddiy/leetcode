import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = 0
        max_so_sar = -sys.maxsize
        for i in range(len(nums)):
            max_ending_here += nums[i]
            max_so_sar = max(max_ending_here, max_so_sar)
            max_ending_here = max(max_ending_here, 0)

        return max_so_sar


solution = Solution().maxSubArray
solution(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
# solution(nums=[1])
# solution(nums=[5, 4, -1, 7, 8])
