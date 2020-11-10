from tools import *


class Solution(object):
    @print_
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        i = 0
        ret = 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            ret += prices[i] - buy
        return ret


solution = Solution().maxProfit

solution([7, 1, 5, 3, 6, 4])
