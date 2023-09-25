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
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] != val:
                i += 1
            while i < j and nums[j] == val:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return sum([1 for x in nums if x != val])


solution = Solution().removeElement

solution([3, 2, 2, 3], 3)
solution([0, 1, 2, 2, 3, 0, 4, 2], 2)
solution([3, 3, 2, 3], 3)
solution([], 0)
solution([3, 3], 3)
