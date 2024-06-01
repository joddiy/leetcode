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
                    while l >= 0 and nums[l] == target:
                        l -= 1
                    while r < n and nums[r] == target:
                        r += 1
                    return l + 1, r - 1
                elif nums[m] > target:
                    return find(i, m - 1)
                else:
                    return find(m + 1, j)

        l, r = find(0, n - 1)
        if r < l:
            return -1, -1
        else:
            return l, r


solution = Solution().searchRange
solution(nums=[5, 7, 7, 8, 8, 10], target=8)
solution(nums=[5, 7, 7, 8, 8, 10], target=6)
solution(nums=[], target=0)
