from tools import *


class Solution(object):
    @print_
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ret = nums[0]
        for idx in range(1, len(nums)):
            ret ^= nums[idx]

        return ret


solution = Solution().singleNumber

solution([2, 2, 1])
