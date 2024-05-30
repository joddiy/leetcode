import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = None
        for n in nums:
            if ret is None:
                ret = n
            else:
                ret = ret ^ n
        return ret


solution = Solution().singleNumber
solution(nums=[2, 2, 1])
solution(nums=[4, 1, 2, 1, 2])
