import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        sum_ = nums[0]
        ret = len(nums) + 1
        while i < len(nums) and j < len(nums):
            if sum_ < target:
                j += 1
                if j < len(nums):
                    sum_ += nums[j]
                else:
                    break
            elif sum_ >= target:
                ret = min(ret, j - i + 1)
                sum_ -= nums[i]
                i += 1
        return ret if ret <= len(nums) else 0


solution = Solution().minSubArrayLen
# solution(target=7, nums=[2, 3, 1, 2, 4, 3])
# solution(target=4, nums=[1, 4, 4])
# solution(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1])
solution(target=11, nums=[1, 2, 3, 4, 5])
