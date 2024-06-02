import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        j = 0
        ret = -sys.maxsize
        cur = 0
        while j < n:
            cur += nums[j]
            ret = max(ret, cur)
            if cur <= 0:
                cur = 0
            j += 1
        return ret


solution = Solution().maxSubArray
solution(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
solution(nums=[1])
solution(nums=[-1])
solution(nums=[0])
solution(nums=[5, 4, -1, 7, 8])
