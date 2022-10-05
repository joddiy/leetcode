from tools import *


class Solution(object):
    @print_
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

solution = Solution().containsDuplicate

solution([1, 2, 3, 1])
