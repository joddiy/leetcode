import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def find(i, j):
            if j < i:
                return i, j
            else:
                m = (i + j) // 2
                if nums[m] == target:
                    l, r = m, m
                    while l >= 0 and nums[l] == target:
                        l -= 1
                    while r < len(nums) and nums[r] == target:
                        r += 1
                    return l + 1, r - 1
                elif nums[m] < target:
                    return find(m + 1, j)
                else:
                    return find(i, m - 1)

        l, r = find(0, len(nums) - 1)
        if r < l:
            return [-1, -1]
        else:
            return [l, r]


solution = Solution().searchRange
solution(nums=[5, 7, 7, 8, 8, 10], target=8)
solution(nums=[5, 7, 7, 8, 8, 10], target=6)
solution(nums=[1], target=1)
solution(nums=[], target=0)
