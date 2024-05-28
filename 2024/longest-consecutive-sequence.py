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
        ret = 0
        for n in nums:
            cur = 0
            if n in set_:
                set_.remove(n)
                cur += 1
                i = n - 1
                while i in set_:
                    set_.remove(i)
                    i -= 1
                    cur += 1
                i = n + 1
                while i in set_:
                    set_.remove(i)
                    i += 1
                    cur += 1
            ret = max(ret, cur)
        return ret


solution = Solution().longestConsecutive
solution(nums=[100, 4, 200, 1, 3, 2])
solution(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
solution(nums=[])
solution(nums=[1])
