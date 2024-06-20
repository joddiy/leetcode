import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        def find(i, j):
            if j < i:
                return i, j
            else:
                m = (i + j) // 2
                if nums[m] == target:
                    l, r = m, m
                    while l > i and nums[l] == target:
                        l -= 1
                    while r < j - 1 and nums[r] == target:
                        r += 1
                    return l, r
                elif nums[m] < target:
                    return find(m + 1, j)
                else:
                    return find(i, m - 1)

        i, j = find(0, n - 1)
        if j < i:
            return [-1, -1]
        return [i, j]


solution = Solution().searchRange
solution(nums=[5, 7, 7, 8, 8, 10], target=8)
solution(nums=[5, 7, 7, 8, 8, 10], target=6)
solution(nums=[], target=0)
