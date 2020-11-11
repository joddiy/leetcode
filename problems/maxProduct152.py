from tools import *


class Solution(object):
    @print_
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = n = p = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            p, n = max(num, p * num, n * num), min(num, p * num, n * num)
            m = max(m, p)
        return m


solution = Solution().maxProduct

solution([2, 3, -2, 4])
solution([-2, 0, -1])