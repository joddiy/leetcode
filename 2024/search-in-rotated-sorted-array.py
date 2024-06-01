import math
import pprint
import sys

from tools import *
from collections import defaultdict


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
            else:
                m = (i + j) // 2
                if nums[m] == target:
                    return m
                if nums[i] <= target < nums[m]:  # right, left
                    return find(i, m - 1)
                if nums[m] < target <= nums[j]:  # left, right
                    return find(m + 1, j)
                if nums[m] <= nums[j]:  # left, left
                    return find(i, m - 1)
                if nums[m] >= nums[i]:  # right, right
                    return find(m + 1, j)

        return find(0, len(nums) - 1)


solution = Solution().search
solution(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
solution(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
solution(nums=[1], target=0)
