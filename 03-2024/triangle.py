import math
import sys

from tools import *
import pprint
from collections import defaultdict


class Solution(object):
    @print_
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []
        for tri in triangle:
            dp.append([0] * len(tri))
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        return min(dp[-1])


solution = Solution().minimumTotal
solution(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
solution(triangle=[[-10]])
