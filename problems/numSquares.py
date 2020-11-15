from tools import *
import math, sys


class Solution(object):
    @print_
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        squares = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            min_v = sys.maxsize
            for j in squares:
                if i - j < 0:
                    break
                min_v = min(min_v, dp[i - j])
            dp[i] = min_v + 1
        return dp[-1]

    @print_
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = set([i**2 for i in range(1, int(math.sqrt(n)) + 1)])

        memo = {}

        def dfs(n, count):
            # returns true of n can be decomposed into 'count' num perf squares
            # ex dfs(12, 3) true
            # ex dfs(12, 2) false

            if (n, count) not in memo:
                if count == 1:
                    return n in square_nums

                memo[n, count] = False
                for k in square_nums:
                    if n - k >= 0 and dfs(n - k, count - 1):
                        memo[n, count] = True
                        break
            return memo[n, count]

        for count in range(1, n + 1):
            if dfs(n, count):
                return count


solution = Solution().numSquares
solution(13)