import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = 0
        n = len(nums)
        while i < n:
            val_ = nums.pop(0)
            if val_ != val:
                nums.append(val_)
                k += 1
            i += 1
        return k


solution = Solution().removeElement
# solution(nums=[3, 2, 2, 3], val=3)
solution(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
