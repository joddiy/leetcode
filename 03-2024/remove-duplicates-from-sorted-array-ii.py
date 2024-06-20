import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            val_ = nums.pop(0)
            if len(nums) >= 2 and nums[0] == nums[1] == val_:
                pass
            else:
                nums.append(val_)
            i += 1
        return len(nums)


solution = Solution().removeDuplicates
solution(nums=[1, 1, 1, 2, 2, 3])
solution(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3])
