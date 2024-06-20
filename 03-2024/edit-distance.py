import math
import sys

from tools import *
import pprint
from collections import defaultdict


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

        def dis(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if memo[i][j] != -1:
                return memo[i][j]
            else:
                if word1[i] == word2[j]:
                    ret = dis(i + 1, j + 1)
                else:
                    ret = min(
                        dis(i + 1, j),  # remove
                        dis(i, j + 1),  # insert
                        dis(i + 1, j + 1),  # replace
                    ) + 1
                memo[i][j] = ret
                return ret

        return dis(0, 0)


solution = Solution().minDistance
solution(word1="horse", word2="ros")
solution(word1="intention", word2="execution")
