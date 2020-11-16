from tools import *


class Solution(object):
    @print_
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set_ = {v: i for i, v in enumerate(nums)}

        for i, v in enumerate(nums):
            if target - v in set_ and set_[target - v] != i:
                return [i, set_[target - v]]


solution = Solution().twoSum

solution(nums=[2, 7, 11, 15], target=9)
solution(nums=[3, 2, 4], target=6)
