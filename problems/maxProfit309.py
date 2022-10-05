from tools import *


class Solution(object):
    @print_
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        buy, sell, cooldown = [0] * n, [0] * n, [0] * n
        bought = buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i] = cooldown[i - 1] - prices[i]
            cooldown[i] = max(buy[i - 1], sell[i - 1], cooldown[i - 1])
            sell[i] = bought + prices[i]
            bought = max(bought, buy[i])
        return max(buy[-1], sell[-1], cooldown[-1])


solution = Solution().maxProfit

solution([1, 2, 3, 0, 2])
