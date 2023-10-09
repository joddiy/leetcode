import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []
        for sub_tri in triangle:
            dp.append([0] * len(sub_tri))
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[-1])


solution = Solution().minimumTotal
solution(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
solution(triangle=[[-10]])
