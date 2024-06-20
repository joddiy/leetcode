import sys

from tools import *
import pprint


class Solution(object):
    @print_
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        buy, sell = -prices[0], 0
        for i in range(1, n):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i])
        return max(buy, sell, 0)


solution = Solution().maxProfit
solution(prices=[7, 1, 5, 3, 6, 4])
solution(prices=[1, 2, 3, 4, 5])
solution(prices=[7, 6, 4, 3, 1])
