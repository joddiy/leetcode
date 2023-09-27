import pprint

from tools import *


class Solution(object):
    @print_
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution 1
        # left = [nums[0]] * len(nums)
        # right = [nums[-1]] * len(nums)
        # for i in range(1, len(nums)):
        #     left[i] = left[i - 1] * nums[i]
        # for i in range(len(nums) - 2, -1, -1):
        #     right[i] = right[i + 1] * nums[i]
        #
        # ret = [0] * len(nums)
        # for i in range(len(nums)):
        #     left_v = left[i - 1] if i - 1 >= 0 else 1
        #     right_v = right[i + 1] if i + 1 < len(nums) else 1
        #     ret[i] = left_v * right_v

        # solution 2
        ret = [1] * len(nums)

        p = 1
        for i in range(len(nums)):
            ret[i] = p
            p *= nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] = p
            p *= nums[i]

        return ret


solution = Solution().productExceptSelf
solution([1, 2, 3, 4])
solution([-1, 1, 0, -3, 3])
