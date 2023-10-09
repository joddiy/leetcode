import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        if dp[-1] > amount:
            return -1
        else:
            return dp[-1]


solution = Solution().coinChange
solution(coins=[1, 2, 5], amount=11)
solution(coins=[2], amount=3)
solution(coins=[1], amount=0)
