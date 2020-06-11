class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for i in range(n)]

        def recursion(i, j):
            if dp[i][j] or j == i+1:
                return dp[i][j]
            coins = 0
            for k in range(i+1, j):
                coins = max(coins, nums[i]*nums[k]*nums[j] +
                            recursion(i, k) + recursion(k, j))
            dp[i][j] = coins
            return coins
        return recursion(0, n-1)

    # Bottom-up
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]  # build the complete array
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n-gap):
                j = i + gap
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k]
                                   * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n-1]


print(Solution().maxCoins([3, 1, 5, 8]))
