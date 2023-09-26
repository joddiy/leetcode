import pprint

from tools import *


class Solution(object):
    @print_
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_i = 0
        for i, s in enumerate(nums):
            if i > max_i:
                return False
            max_i = max(max_i, i + s)
        return True


solution = Solution().canJump
solution([2, 3, 1, 1, 4])
solution([3, 2, 1, 0, 4])
