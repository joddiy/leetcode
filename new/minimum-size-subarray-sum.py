from tools import *
import pprint


class Solution(object):
    @print_
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        nums = [0] + nums
        i, j = 0, 0
        sum_ = 0
        ret = len(nums) + 1
        while j < len(nums) - 1:
            while j < len(nums) - 1 and sum_ < target:
                j += 1
                sum_ += nums[j]
            while i < j and sum_ >= target:
                ret = min(ret, j - i)
                i += 1
                sum_ -= nums[i]
        if ret == len(nums) + 1:
            return 0
        else:
            return ret


solution = Solution().minSubArrayLen
solution(target=7, nums=[2, 3, 1, 2, 4, 3])
solution(target=4, nums=[1, 4, 4])
solution(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1])
solution(target=213, nums=[12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12])
