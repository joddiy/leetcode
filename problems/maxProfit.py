from tools import *
import sys


class Solution(object):
    @print_
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        max_ = 0
        for i in range(len(prices) - 1, -1, -1):
            max_ = max(max_, prices[i])
            ret = max(ret, max_ - prices[i])
        return ret


solution = Solution().maxProfit

solution([7, 1, 5, 3, 6, 4])
solution([7, 6, 4, 3, 1])
solution([])
solution([1])
