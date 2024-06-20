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
        n = len(nums)
        i, j = 0, 0
        cur_ = nums[0]
        ret = sys.maxsize
        while i < n and j < n:
            if cur_ < target:
                j += 1
                if j >= n:
                    break
                cur_ += nums[j]
            else:
                ret = min(ret, j - i + 1)
                cur_ -= nums[i]
                i += 1

        if ret == sys.maxsize:
            return 0
        else:
            return ret


solution = Solution().minSubArrayLen
solution(target=7, nums=[2, 3, 1, 2, 4, 3])
solution(target=4, nums=[1, 4, 4])
solution(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1])
solution(target=11, nums=[1, 2, 3, 4, 5])
