from tools import *
import collections


class Solution(object):
    @print_
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_ = sum(nums)
        if sum_ < S:
            return 0
        n = len(nums)
        dp = [0] * (2 * sum_ + 1)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        for i in range(1, n):
            num = nums[i]
            dp_ = [0] * (2 * sum_ + 1)
            for j in range(-sum_, sum_ + 1):
                if j + num <= sum_:
                    dp_[j] += dp[j + num]
                if j - num >= -sum_:
                    dp_[j] += dp[j - num]
            dp = dp_
        return dp[S]

    @print_
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if sum(nums) < S:
            return 0
        # O(l*n), O(n)
        dp = collections.defaultdict(int)
        dp[0] = 1  # Don't forget to initialize!
        for n in nums:
            ndp = collections.defaultdict(int)
            #for sgn in (1, -1):
            for k in dp.keys():
                ndp[k + n] += dp[k]
                ndp[k - n] += dp[k]
            dp = ndp
        return dp[S]


solution = Solution().findTargetSumWays

solution([1, 1, 1, 1, 1], 3)
solution([1], 2)