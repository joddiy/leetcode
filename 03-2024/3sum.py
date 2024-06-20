import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        map_ = {}
        for i, n in enumerate(nums):
            map_[n] = i
        ret = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                val = -(nums[i] + nums[j])
                if val in map_ and map_[val] > j:
                    ret.add((nums[i], nums[j], val))
        return list(ret)


solution = Solution().threeSum
solution(nums=[-1, 0, 1, 2, -1, -4])
solution(nums=[0, 0, 0, 0])
