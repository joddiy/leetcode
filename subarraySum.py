class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(nums)
        n, m = len(nums), 2 * k + 1

        dp = [[0, 0] * m for _ in range(n + 1)]
        dp[0][nums[0]] = 1

        for i in range(n):
            for j in range(nums[i], m - nums[i]):
                if dp[i][j]:
                    dp[i + 1][j - nums[i]] += dp[i][j]
                    dp[i + 1][j] += dp[i][j]

        print(dp)
        return dp[-1][s + k]


Solution().subarraySum([1, 1, 1], 2)
