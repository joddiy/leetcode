import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i - c] + 1, dp[i])
                    
        if dp[-1] == sys.maxsize:
            return -1
        else:
            return dp[-1]


solution = Solution().coinChange
solution(coins=[1, 2, 5], amount=11)
# solution(coins=[2], amount=3)
# solution(coins=[1], amount=0)
