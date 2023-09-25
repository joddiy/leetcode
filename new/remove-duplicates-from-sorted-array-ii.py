import pprint

from tools import *


class Solution(object):
    @print_
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if i == 0 or i == 1:
                i += 1
            elif nums[i] == nums[i - 2]:
                nums.pop(i)
            else:
                i += 1
        return i


solution = Solution().removeDuplicates

solution([0, 0, 1, 1, 1, 1, 2, 3, 3])
