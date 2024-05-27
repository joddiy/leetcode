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
        map_ = {v: k for k, v in enumerate(nums)}
        vis_ = defaultdict(set)
        ret = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                target = 0 - nums[i] - nums[j]
                if target in map_ and map_[target] > j and nums[j] not in vis_[nums[i]]:
                    ret.append([nums[i], nums[j], target])
                    vis_[nums[i]].add(nums[j])
        return ret


solution = Solution().threeSum
# solution(nums=[-1, 0, 1, 2, -1, -4])
solution(nums=[0, 0, 0, 0])
