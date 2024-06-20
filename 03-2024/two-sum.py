import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_ = defaultdict(list)
        for i, n in enumerate(nums):
            map_[n].append(i)
        ret = None
        for i in range(len(nums)):
            j = target - nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if j == nums[i] and len(map_[j]) > 1:
                return map_[j]
            elif j in map_ and map_[j][0] > i:
                return [i, map_[j][0]]


solution = Solution().twoSum
solution(nums=[2, 7, 11, 15], target=9)
solution(nums=[3, 2, 4], target=6)
solution(nums=[3, 3], target=6)
