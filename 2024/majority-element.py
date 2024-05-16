import sys

from tools import *
import pprint


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max, cur_max_cnt = None, 0
        for num in nums:
            if cur_max_cnt == 0:
                cur_max = num
                cur_max_cnt = 1
            elif num == cur_max:
                cur_max_cnt += 1
            else:
                cur_max_cnt -= 1
        return cur_max


solution = Solution().majorityElement
# solution(nums=[3, 2, 3])
solution(nums=[2, 2, 1, 1, 1, 2, 2])
