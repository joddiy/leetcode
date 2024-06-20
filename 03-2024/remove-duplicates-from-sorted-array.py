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
        i, k, n = 0, 0, len(nums)
        while i < n:
            val_ = nums.pop(0)
            if len(nums) > 0 and val_ == nums[0]:
                pass
            else:
                nums.append(val_)
                k += 1
            i += 1
        return k


solution = Solution().removeDuplicates
solution(nums=[1, 1, 2])
solution(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
solution(nums=[1])
solution(nums=[1, 1])
solution(nums=[])
