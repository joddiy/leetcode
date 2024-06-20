import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums.pop()
        while nums:
            ret = ret ^ nums.pop()
        return ret


solution = Solution().singleNumber
solution(nums=[2, 2, 1])
solution(nums=[4, 1, 2, 1, 2])
