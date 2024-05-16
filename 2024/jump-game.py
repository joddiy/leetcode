import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = cur_max = 0
        while i <= cur_max and i < len(nums):
            cur_max = max(cur_max, nums[i] + i)
            i += 1
        return i == len(nums)


solution = Solution().canJump
solution(nums=[2, 3, 1, 1, 4])
solution(nums=[3, 2, 1, 0, 4])
solution(nums=[3])
