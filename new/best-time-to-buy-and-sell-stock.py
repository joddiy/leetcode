import pprint

from tools import *


class Solution(object):
    @print_
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # solution 1
        # dp = [0] * len(prices)
        # dp[-1] = prices[-1]
        # for i in range(len(prices) - 2, -1, -1):
        #     dp[i] = max(prices[i], dp[i + 1])
        # return max(max([dp[i] - prices[i] for i in range(len(prices))]), 0)

        # solution 1
        max_s = prices[-1]
        max_p = prices[-1] - max_s
        for i in range(len(prices) - 2, -1, -1):
            max_s = max(prices[i], max_s)
            max_p = max(max_s - prices[i], max_p)
        return max(max_p, 0)


solution = Solution().maxProfit

solution([7, 1, 5, 3, 6, 4])
solution([7, 6, 4, 3, 1])
