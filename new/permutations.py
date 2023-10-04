import math
import pprint
import sys

from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        ll = len(nums)

        def recursive(cur_ret, i):
            num = nums.pop(i)
            if len(nums) == 0:
                ret.append(cur_ret + [num])
            else:
                for j in range(len(nums)):
                    recursive(cur_ret + [num], j)
            nums.insert(i, num)

        for i in range(ll):
            recursive([], i)
        return ret


solution = Solution().permute
solution([1, 2, 3])
solution([0, 1])
solution([1])
solution([1, 2, 4, 5])
