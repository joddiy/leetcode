import pprint

from tools import *


class Solution(object):
    @print_
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp_2_hold, dp_2_sell = -float('inf'), 0
        dp_1_hold, dp_1_sell = -float('inf'), 0

        for stock_price in prices:
            # either keep being in not-hold state, or sell with stock price today
            dp_1_sell = max(dp_1_sell, dp_1_hold + stock_price)

            # either keep being in hold state, or just buy with stock price today ( add one more transaction )
            dp_1_hold = max(dp_1_hold, 0 - stock_price)

            # either keep being in not-hold state, or sell with stock price today
            dp_2_sell = max(dp_2_sell, dp_2_hold + stock_price)

            # either keep being in hold state, or just buy with stock price today ( add one more transaction )
            dp_2_hold = max(dp_2_hold, dp_1_sell - stock_price)

        return dp_2_sell


solution = Solution().maxProfit

solution(prices=[3, 3, 5, 0, 0, 3, 1, 4])
solution(prices=[1, 2, 3, 4, 5])
solution(prices=[7, 6, 4, 3, 1])
