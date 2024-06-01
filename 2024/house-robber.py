import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        pre = [nums[0], 0]
        for i in range(1, len(nums)):
            pre = [pre[1] + nums[i], max(pre)]
        return max(pre)


solution = Solution().rob
solution(nums=[1, 2, 3, 1])
solution(nums=[2, 7, 9, 3, 1])
