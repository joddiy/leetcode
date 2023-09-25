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
            if i == 0:
                i += 1
            elif nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return i


solution = Solution().removeDuplicates

solution([1, 1, 2])
solution([1, 1])
