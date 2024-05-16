import sys

from tools import *
import pprint


class Solution(object):
    # @print_
    # def jump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     cur_stp = [sys.maxsize] * n
    #     cur_stp[0] = 0
    #     for i in range(n):
    #         for j in range(1, nums[i] + 1):
    #             if i + j >= n:
    #                 break
    #             cur_stp[i + j] = min(cur_stp[i + j], cur_stp[i] + 1)
    #     return cur_stp[-1]

    @print_
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ret = l = r = 0
        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            ret += 1
        return ret


solution = Solution().jump
solution(nums=[2, 3, 1, 1, 4])
solution(nums=[2, 3, 0, 1, 4])
solution(nums=[3])
