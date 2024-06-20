import sys

from tools import *
import pprint


class Solution(object):

    @print_
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_ = [sys.maxsize] * len(nums)
        cur_max = 0
        min_[0] = 0
        for i in range(n):
            cur_max = max(cur_max, i + nums[i])
            for j in range(i + 1, cur_max + 1):
                if j < n:
                    min_[j] = min(min_[j], min_[i] + 1)

        return min_[-1]


solution = Solution().jump
solution(nums=[2, 3, 1, 1, 4])
solution(nums=[2, 3, 0, 1, 4])
solution(nums=[3])
solution(nums=[0])
