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
        buy = [0] * n
        sell = [0] * n
        buy[0] = - prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return max(buy[-1], sell[-1])


solution = Solution().maxProfit
solution(prices=[7, 1, 5, 3, 6, 4])
solution(prices=[1, 2, 3, 4, 5])
solution(prices=[7, 6, 4, 3, 1])
