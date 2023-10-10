import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m > n:
            word1, word2, m, n = word2, word1, n, m
        memo = [[-1] * (n + 1) for _ in range(m + 1)]

        def distance(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if memo[i][j] != -1:
                return memo[i][j]
            if word1[i] == word2[j]:
                dis_ = distance(i + 1, j + 1)
            else:
                dis_ = min(
                    distance(i + 1, j),  # delete
                    distance(i, j + 1),  # insert
                    distance(i + 1, j + 1),  # replace
                ) + 1
            memo[i][j] = dis_
            return dis_

        return distance(0, 0)


solution = Solution().minDistance
solution(word1="horse", word2="ros")
solution(word1="intention", word2="execution")
