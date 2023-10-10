import math
import pprint
import sys

from tools import *
from collections import defaultdict

import heapq


class Solution(object):
    @print_
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        w = len(s3)
        if w != m + n:
            return False
        if m == 0:
            return s2 == s3
        if n == 0:
            return s1 == s3

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                if s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]


solution = Solution().isInterleave
solution(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
solution(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
solution(s1="", s2="", s3="")
solution(s1="a", s2="b", s3="ab")
