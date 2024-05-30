import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret = []
        n = len(nums)

        def recursive(i, prefix):
            num = nums.pop(i)
            if len(nums) == 0:
                ret.append(prefix + [num])
            else:
                for j in range(len(nums)):
                    recursive(j, prefix + [num])
            nums.insert(i, num)

        for i in range(n):
            recursive(i, [])
        return ret


solution = Solution().permute
solution(nums=[1, 2, 3])
