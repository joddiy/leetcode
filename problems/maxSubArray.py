from tools import *
import sys


class Solution(object):
    # O(n)
    @print_
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        least_sum = 0
        ret = -sys.maxsize
        for i in range(len(nums)):
            cur_sum += nums[i]
            ret = max(ret, cur_sum - least_sum)
            # update least_sum after the ret
            # because we don't want cur_sum - cur_sum
            least_sum = min(least_sum, cur_sum)
        return ret
    
    @print_
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        least_sum = 0
        ret = -sys.maxsize
        for i in range(len(nums)):
            cur_sum += nums[i]
            ret = max(ret, cur_sum - least_sum)
            # update least_sum after the ret
            # because we don't want cur_sum - cur_sum
            least_sum = min(least_sum, cur_sum)
        return ret


solution = Solution().maxSubArray

solution([-2, 1, -3, 4, -1, 2, 1, -5, 4])
solution([1])
solution([-1])
solution([-2, -1])
solution([1, 2])
solution([1, -2])
solution([-1, 2])