import sys

from tools import *
import pprint
from collections import Counter


class Solution(object):
    @print_
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_ = set(nums)
        n = len(nums)
        max_ = 0
        for i in range(n):
            val = nums[i]
            if val in set_:
                set_.remove(val)
                ret = 1
                l = val - 1
                while l in set_:
                    set_.remove(l)
                    l -= 1
                    ret += 1
                r = val + 1
                while r in set_:
                    set_.remove(r)
                    r += 1
                    ret += 1
                max_ = max(max_, ret)
        return max_


solution = Solution().longestConsecutive
solution(nums=[100, 4, 200, 1, 3, 2])
solution(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
solution(nums=[])
solution(nums=[1])
