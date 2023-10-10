import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]


solution = Solution().uniquePathsWithObstacles
solution(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]])
solution(obstacleGrid=[[0, 1], [0, 0]])
solution(obstacleGrid=[[1, 0]])
