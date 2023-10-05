import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def find(i, j):
            if j < i:
                return nums[i]
            m = (i + j) // 2
            if nums[m] < nums[m - 1]:  # minium is its self
                return nums[m]
            elif nums[j] < nums[m]:  # minium at right
                return find(m + 1, j)
            else:
                return find(i, m - 1)  # minium at left

        return find(0, len(nums) - 1)


solution = Solution().findMin
solution(nums=[3, 4, 5, 1, 2])
solution(nums=[4, 5, 6, 7, 0, 1, 2])
solution(nums=[11, 13, 15, 17])
solution(nums=[3, 1, 2])
solution(nums=[5, 1, 2, 3, 4])
