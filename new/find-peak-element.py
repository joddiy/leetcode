import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-sys.maxsize] + nums + [-sys.maxsize]

        def find(i, j):
            if i == j:
                return i
            m = (i + j) // 2
            if nums[m] < nums[m - 1]:
                return find(i, m - 1)
            elif nums[m] < nums[m + 1]:
                return find(m + 1, j)
            else:
                return m

        return find(0, len(nums) - 1) - 1


solution = Solution().findPeakElement
solution(nums=[1, 2, 3, 1])
solution(nums=[1, 2, 1, 3, 5, 6, 4])
