import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones

        return ones


solution = Solution().singleNumber
solution(nums=[2, 2, 3, 2])
solution(nums=[0, 1, 0, 1, 0, 1, 99])
