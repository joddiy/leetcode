import pprint

from tools import *


class Solution(object):
    @print_
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return i


solution = Solution().removeElement

solution([3, 2, 2, 3], 3)
solution([0, 1, 2, 2, 3, 0, 4, 2], 2)
solution([3, 3, 2, 3], 3)
solution([], 0)
solution([3, 3], 3)
solution([0, 1, 2, 2, 3, 0, 4, 2], 2)
