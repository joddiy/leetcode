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
        cur_sum = 0
        ret = -sys.maxsize
        i = 0
        while i < n:
            cur_sum += nums[i]
            ret = max(ret, cur_sum)
            cur_sum = max(cur_sum, 0)
            i += 1
        return ret


solution = Solution().maxSubArray
solution(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
solution(nums=[1])
solution(nums=[-1])
solution(nums=[-1, -2])
solution(nums=[0])
solution(nums=[5, 4, -1, 7, 8])
