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
                coins = max(coins, nums[i]*nums[k] *
                            nums[j]+recursion(i, k)+recursion(k, j))
            dp[i][j] = coins
            return coins
        return recursion(0, n-1)

    def maxCoins2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(n-length):
                j = i + length
                mij = nums[i] * nums[j]
                for mid in range(i + 1, j):
                    v = dp[i][mid] + dp[mid][j] + mij * nums[mid]
                    print(i,j,mid,v)
                    if v > dp[i][j]:
                        dp[i][j] = v

        return dp[0][n-1]


Solution().maxCoins2([3, 1, 5, 8])
