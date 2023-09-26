import pprint

from tools import *


class Solution(object):
    @print_
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        print(buy, sell)
        return max(buy[-1], sell[-1])


solution = Solution().maxProfit

solution([7, 1, 5, 3, 6, 4])
solution([7])
