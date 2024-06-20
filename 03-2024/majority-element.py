import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_, cnt_ = None, 0
        for n in nums:
            if cnt_ == 0:
                max_ = n
                cnt_ = 1
            elif n == max_:
                cnt_ += 1
            else:
                cnt_ -= 1
        return max_


solution = Solution().majorityElement
solution(nums=[3, 2, 3])
solution(nums=[2, 2, 1, 1, 1, 2, 2])
