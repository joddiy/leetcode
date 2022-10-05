from tools import *


class Solution(object):
    @print_
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_v = None
        cur_c = 0
        for i in range(len(nums)):
            if cur_c == 0:
                cur_v = nums[i]
                cur_c = 1
            elif nums[i] == cur_v:
                cur_c += 1
            else:
                cur_c -= 1

        return cur_v


solution = Solution().majorityElement

solution([2, 2, 1, 1, 1, 2, 2])
