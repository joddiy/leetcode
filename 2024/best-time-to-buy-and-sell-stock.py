import sys

from tools import *
import pprint


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        min_left = sys.maxsize
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, prices[i] - min_left)
            min_left = min(min_left, prices[i])
        return max_profit


solution = Solution().maxProfit
solution(prices=[7, 1, 5, 3, 6, 4])
solution(prices=[7, 6, 4, 3, 1])
