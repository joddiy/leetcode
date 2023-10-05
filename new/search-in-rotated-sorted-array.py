import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find(i, j):
            if j < i:
                return -1
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[i] <= target < nums[m]:  # pivot at right, and target may at left
                return find(i, m - 1)
            elif nums[m] < target <= nums[j]:  # pivot at left, and target may at right
                return find(m + 1, j)
            elif nums[m] <= nums[j]:  # pivot at left, and target may at left
                return find(i, m - 1)
            elif nums[i] <= nums[m]:  # pivot at right, and target may at right
                return find(m + 1, j)

        return find(0, len(nums) - 1)


solution = Solution().search
solution(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
solution(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
solution(nums=[1], target=0)
solution(nums=[1, 3], target=3)
