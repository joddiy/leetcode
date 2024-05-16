import sys

from tools import *
import pprint


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, n = 0, len(nums)
        k = 0
        while i < n:
            _val = nums.pop(0)
            if _val != val:
                nums.append(_val)
            else:
                k += 1
            i += 1
        return k


solution = Solution().removeElement
solution(nums=[3, 2, 2, 3], val=3)
solution(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
