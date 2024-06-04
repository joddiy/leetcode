import pprint

from tools import *


class Solution(object):
    @print_
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        buy = [float('inf')] * k
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(k):
                if price - sell[i - 1] < buy[i]:
                    buy[i] = price - sell[i - 1]
                if price - buy[i] > sell[i]:
                    sell[i] = price - buy[i]

        return sell[-2]


solution = Solution().maxProfit

solution(k=2, prices=[2, 4, 1])
solution(k=2, prices=[3, 2, 6, 5, 0, 3])
