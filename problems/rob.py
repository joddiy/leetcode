from tools import *


class Solution(object):
    @print_
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = dp[i - 1]
            dp[i] = max(dp[i], nums[i - 1] + dp[i - 2])
        return dp[-1]

    @print_
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        last, now = 0, nums[0]
        for i in range(2, len(nums) + 1):
            now, last = max(now, nums[i - 1] + last), now
        return now


solution = Solution().rob

solution([1, 2, 3, 1])
solution([2, 7, 9, 3, 1])
solution([])