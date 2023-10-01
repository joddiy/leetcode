import math
import pprint
from tools import *
from collections import defaultdict


class Solution(object):
    @print_
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


solution = Solution().climbStairs
solution(n=2)
solution(n=3)
