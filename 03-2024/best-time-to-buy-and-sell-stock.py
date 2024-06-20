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
        left_min = sys.maxsize
        ret = -sys.maxsize
        for i in range(n):
            left_min = min(left_min, prices[i])
            ret = max(ret, prices[i] - left_min, 0)
        return ret

solution = Solution().maxProfit
solution(prices=[7, 1, 5, 3, 6, 4])
solution(prices=[7, 6, 4, 3, 1])
