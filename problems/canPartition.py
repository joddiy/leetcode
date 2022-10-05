from tools import *


class Solution(object):
    @print_
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        nums = sorted(nums)
        memo = {}

        def dfs(nums, target):
            for i, num in enumerate(target):
                sub_ = target - num
                if sub_ == 0:
                    return True
                elif sub_ < 0:
                elif dfs(, sub_):
                    # nums[i + 1:] means
                    return True
            return False

        return dfs(nums, sum_ // 2)

    @print_
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        sum_v = sum(nums)
        if sum_v % 2 == 1:
            return False
        if max(nums) > sum_v // 2:
            return False
        scale = sum_v // 2 + 1
        dp = [[False] * scale for _ in range(len(nums))]

        nums = sorted(nums, reverse=True)
        dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            dp[i][nums[i]] = True
            for j in range(scale - 1, 0, -1):
                if dp[i - 1][j]:
                    dp[i][j] = True
                if j > nums[i] and dp[i - 1][j - nums[i]]:
                    dp[i][j] = True
                if dp[i][-1]:
                    return True
        return dp[-1][-1]
