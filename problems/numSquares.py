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
        self.squares = [i**2 for i in range(int(math.sqrt(n)), 0, -1)]

        self.ret = n + 1
        l = len(self.squares)

        def dfs(cur_amount, cur_count, idx):
            if idx >= l or cur_amount < 0:
                return

            coin = self.squares[idx]
            # if max amount by current coin larger than ret
            if cur_count + cur_amount // coin + (cur_amount % coin !=
                                                 0) >= self.ret:
                return

            # if amount can be divided by current coin
            if cur_amount % coin == 0:
                self.ret = min(self.ret, cur_count + cur_amount // coin)
                return

            # try biggest coin
            dfs(cur_amount - coin, cur_count + 1, idx)

            # try next coin
            dfs(cur_amount, cur_count, idx + 1)

        dfs(n, 0, 0)
        if self.ret == n + 1:
            return -1
        else:
            return self.ret

    @print_
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
        memo = {}

        def dfs(n, count):
            # returns true of n can be decomposed into 'count' num perf squares
            # ex dfs(12, 3) true
            # ex dfs(12, 2) false
            if (n, count) not in memo:
                if count == 1:
                    return n in squares

                memo[n, count] = False
                for i in squares:
                    if n - i < 0:
                        break
                    elif dfs(n - i, count - 1):
                        memo[n, count] = True
                        break
            return memo[n, count]

        for i in range(1, n + 1):
            if dfs(n, i):
                return i


solution = Solution().numSquares
# solution(13)
solution(12)