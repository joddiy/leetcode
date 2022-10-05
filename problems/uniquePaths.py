from tools import *


class Solution(object):
    @print_
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


solution = Solution().uniquePaths

solution(3, 2)
solution(3, 7)
solution(1, 0)
solution(1, 1)