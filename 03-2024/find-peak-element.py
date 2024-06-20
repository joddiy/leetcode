import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-sys.maxsize] + nums + [-sys.maxsize]

        def find(i, j):
            if j < i:
                return j
            else:
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
solution(nums=[3, 2, 1])
