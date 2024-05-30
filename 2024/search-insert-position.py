import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find(i, j):
            if j < i:
                return j
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return find(i, m - 1)
            else:
                return find(m + 1, j)

        p = find(0, len(nums) - 1)
        if nums[p] == target:
            return p
        else:
            return p + 1


solution = Solution().searchInsert
solution(nums=[1, 3, 5, 6], target=5)
