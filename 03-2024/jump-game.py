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
        n = len(nums)
        cur_max = nums[0]
        for i in range(1, n):
            if i <= cur_max:
                cur_max = max(cur_max, i + nums[i])
            else:
                return False
        return True


solution = Solution().canJump
solution(nums=[2, 3, 1, 1, 4])
solution(nums=[3, 2, 1, 0, 4])
solution(nums=[3])
