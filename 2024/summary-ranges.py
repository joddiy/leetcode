import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        for i, n in enumerate(nums):
            if i == 0:
                ret.append([n])
            elif nums[i] == nums[i - 1] + 1:
                if i == len(nums) - 1:
                    if nums[i] != ret[-1][0]:
                        ret[-1].append(nums[i])
            else:
                if nums[i - 1] != ret[-1][0]:
                    ret[-1].append(nums[i - 1])
                ret.append([n])
        return ["->".join(str(y) for y in x) for x in ret]


solution = Solution().summaryRanges
solution(nums=[0, 1, 2, 4, 5, 7])
solution(nums=[0, 2, 3, 4, 6, 8, 9])
